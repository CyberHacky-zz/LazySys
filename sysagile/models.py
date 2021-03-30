from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email


class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirmpassword = models.CharField(max_length=30)

    def __str__(self):
        return self.username + ' - ' + self.name + ' - ' + self.email
