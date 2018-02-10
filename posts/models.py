from django.db import models


# Create your models here.
class SignInModel(models.Model):
    uname = models.CharField(max_length=20, null=False)
    passwd = models.CharField(max_length=20, null=False)
    