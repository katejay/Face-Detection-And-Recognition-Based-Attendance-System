package com.example.smartattendance;

public class UploadFile {

    public String name;
    public String url;

    public UploadFile() {
    }

    public UploadFile(String name, String url) {
        this.name = name;
        this.url = url;
    }

    public String getName() {
        return name;
    }

    public String getUrl() {
        return url;
    }
}
