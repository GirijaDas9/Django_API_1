from django.db import models
from utils.models import TimeStamp
from django.contrib.auth import get_user_model
# Create your models here.

class List(TimeStamp, models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class ListItem(TimeStamp, models.Model):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text