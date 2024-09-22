from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

class DetectSpammerManager(BaseUserManager):
    def create_user(self, phone_number, password=None, name=None, email=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        user = self.model(phone_number=phone_number, name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, name=None, email=None):
        user = self.create_user(phone_number, password, name, email)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class DetectSpammer(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, null=True,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = DetectSpammerManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

class Spam(models.Model):
    phone_number = models.CharField(max_length=15,null=True)
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.phone_number} marked as spam by {self.reported_by}'

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contacts', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=100)
