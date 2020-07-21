from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    content = models.CharField(max_length=400)
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email Required")
        if not username:
            raise ValueError("Username Required")
        
        user=self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email          = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username       = models.CharField(max_length=30, unique=True)
    date_joined    = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login     = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin       = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=True)
    is_superuser   = models.BooleanField(default=False)
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_model_perms(self, app_label):
        return True
