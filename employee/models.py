from django.db import models  
class Employee(models.Model):  
    empid = models.CharField(max_length=20)  
    empname = models.CharField(max_length=100)  
    empemail = models.EmailField()  
    empcontact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  