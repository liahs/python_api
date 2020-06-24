from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    real_name=models.CharField(max_length=300)
    tz=models.CharField(max_length=200)

    def __str__(self):
        return self.real_name

class ActivityModel(models.Model):
    user=models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.user.real_name