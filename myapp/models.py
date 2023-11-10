from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_detail(models.Model):
    user_detail_name = models.TextField()
    user_detail_email = models.TextField()
    user_detail_address = models.TextField()
    user_detail_phone = models.TextField()
    user_detail_otp = models.TextField()
    user_detail_password = models.TextField()

    def __str__(self):
        return f"{self.user_detail_name} ({self.user_detail_email})"


class Customer(models.Model):
    username = models.TextField()
    name = models.TextField()
    email = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    gstnumber = models.TextField()
    mailreminder = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"



    
class ChatMess(models.Model):
    sender_email = models.TextField()
    receiver_email = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.sender_email} to {self.receiver_email}: {self.message}"