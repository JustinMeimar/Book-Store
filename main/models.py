from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    content = models.CharField(max_length=200)
    title = models.CharField(max_length=40)
    picture = models.ImageField(upload_to="main/images",blank=False,null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

# class User(AbstractBaseUser):
#     email = models.

 