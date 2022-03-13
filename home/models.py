from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message =  models.TextField()

    def __str__(self) :
        return self.name
    

class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    created_date = models.DateTimeField( auto_now_add=True)
    
    def __str__(self) :
        return self.branch_name

class Teacher(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    phone_teacher = models.CharField( max_length=75)
    email_teacher = models.EmailField( max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    image = models.ImageField(upload_to = 'teacher',default = 'default.png')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return super().__str__()