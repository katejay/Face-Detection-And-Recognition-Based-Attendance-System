import cv2,os
import csv
import pandas as pd
import datetime
import time
import pyrebase
from firebase import firebase
from google.cloud import storage
from google.cloud.storage.blob import Blob

config = {
    "apiKey": "Enter here apiKey",
    "authDomain": "Enter here authDomain",
    "databaseURL": "Enter here databaseURL",
    "projectId": "Enter here projectId",
    "storageBucket": "Enter here storageBucket",
    "messagingSenderId": "Enter here messagingSenderId",
    "appId": "Enter here appId"
}

firebase = firebase.FirebaseApplication("https://Enter here databaseURL", None)
blob = Blob.from_string("gs://Enter here storageBucket path")

def trackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("DataSet\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)   
    df=pd.read_csv("StudentRecord.csv")
    
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("UnknownImages"))+1
                cv2.imwrite("UnknownImages\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first') 

        cv2.imshow('Face Recognizing',im)
        pass

        if cv2.waitKey(10000):
            break

    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")

    #fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+".csv"
    attendance.to_csv(fileName,index=False)
    Firebase = pyrebase.initialize_app(config)
    storage = Firebase.storage()
    blob = storage.child('uploads/'+ fileName).put(fileName)
    #jay = storage.child().get_url(blob['downloadTokens'])
    
    data =  { 'name': "Date_"+date+"  Time_"+Hour+"-"+Minute+"-"+Second, 'url': "https://firebasestorage.googleapis.com/v0/b/ <Enter here storageBucket path> %2FAttendance%5CAttendance_"+date+"_"+Hour+"-"+Minute+".csv?alt=media&token="+blob['downloadTokens']}
    #data =  { 'name': "Date_"+date+"  Time_"+Hour+"-"+Minute+"-"+Second, 'url': jay}
    result = firebase.post('/uploads',data)
    print(result)

    cam.release()
    cv2.destroyAllWindows()

trackImages()