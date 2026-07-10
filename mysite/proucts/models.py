from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class  Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Phone(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    img = models.ImageField(upload_to="phones/",null=True,blank=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    stock = models.PositiveBigIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return  f"{self.brand} {self.model}"