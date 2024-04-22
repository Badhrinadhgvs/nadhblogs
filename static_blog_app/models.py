from django.db import models

# Create your models here.


class Des(models.Model):
    Title=models.CharField(max_length=20)
    Desc=models.TextField()

    def __str__(self):
        return self.Title
    
    
    
class writ(models.Model):
    tit=models.CharField(max_length=10)
    email=models.EmailField()
    con=models.TextField()
    
    
    def __str__(self):
        return self.tit
 
 
class Useradd(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

 
 
class alls(models.Model):
    stock=models.ForeignKey(Des,on_delete=models.CASCADE) 
        