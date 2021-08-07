from django.db import models
from django.contrib.auth import get_user_model
from utils.models import TimeStamp



class Task(TimeStamp,models.Model):
    user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)


    def __str__(self):
        return self.title
