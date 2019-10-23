package com.example.smartattendance;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

public class FetchActivity extends AppCompatActivity {

    Button fetch;

    FirebaseStorage storage;
    FirebaseDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fetch);


        fetch=findViewById(R.id.fetchFiles);
        fetch.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                startActivity(new Intent(FetchActivity.this, MyRecyclerViewActivity.class));

            }
        });

        storage=FirebaseStorage.getInstance();
        database=FirebaseDatabase.getInstance();

    }


}
