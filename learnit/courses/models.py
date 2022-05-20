from email.policy import default
from django.db import models
from django.utils import timezone

class Category(models.Model):
    parent_category = models.Model('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    priority = models.IntegerChoices(default=0)
    is_published = models.BooleanField()
    

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    playlist_id = models.CharField(max_length=200)
    playlist_url = models.CharField(max_length=200)
    priority = models.IntegerChoices(default=0)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    is_published = models.BooleanField()
    
