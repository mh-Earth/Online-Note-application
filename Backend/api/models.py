from pydoc import describe
from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(primary_key=True,max_length=8)
    user_name = models.CharField(max_length=50,default=f"user {id}")
    first_name = models.CharField(max_length=32,default="")
    last_name = models.CharField(max_length=32,default="")
    password = models.CharField(max_length=32 , default="1234")
    date_of_creat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    

class Note(models.Model):
    title = models.CharField(max_length=32,default="untitled")
    describe = models.CharField(max_length=1024,default="undescribe")


    def __str__(self):
        return self.title
    
