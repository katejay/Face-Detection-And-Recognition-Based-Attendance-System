package com.example.smartattendance;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.jar.Attributes;

public class RegistrationadminActivity extends AppCompatActivity {


    private EditText Name;
    private EditText Password;
    private Button Login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registrationadmin);


        Name = (EditText)findViewById(R.id.etName1);
        Password = (EditText)findViewById(R.id.etPassword1);
        Login = (Button)findViewById(R.id.btnLogin1);

    Login.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            validate(Name.getText().toString(), Password.getText().toString());
                    }
    });
    }

    private void validate(String userName, String userPassword){
        if((userName.equals("Admin")) && (userPassword.equals("1234"))){
            Intent intent = new Intent(RegistrationadminActivity.this, RegistrationActivity.class);
            startActivity(intent);
        }
    }


}
