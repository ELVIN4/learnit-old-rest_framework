from email.mime import image
from tabnanny import verbose
from django.db import models

from colorfield.fields import ColorField


class Languare(models.Model):
    name = models.CharField(max_length=40)
    priority = models.IntegerField(default=0)
    is_published = models.BooleanField()
        
    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['-priority']

    def __str__(self):
        return self.name

class ImageStyle(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/category/styles/')
    bg_color = ColorField()
    title_color = ColorField()
    watemark = models.CharField(max_length=80)
    watemark_color = ColorField(default='#AEAEAE')

    class Meta:
        verbose_name = 'Стиль изображения'
        verbose_name_plural = 'Стили изображений'
    
    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    parent_category = models.ForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
        )
    image = models.ImageField(upload_to='courses/category/%Y/%m/%d/')
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    languare = models.ForeignKey(Languare, on_delete=models.PROTECT)
    image_style = models.ForeignKey(
        ImageStyle, 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True
        )    
    is_published = models.BooleanField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-priority']

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    playlist_image_url = models.CharField(max_length=200)
    playlist_title = models.CharField(max_length=500)
    playlist_views = models.IntegerField(default=0)
    playlist_id = models.CharField(max_length=200, unique=True)
    playlist_url = models.CharField(max_length=300)
    playlist_videos_count = models.IntegerField(default=1)
    playlist_owner = models.CharField(max_length=500)
    playlist_owner_url = models.CharField(max_length=500)
    priority = models.IntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    languare = models.ForeignKey(Languare, on_delete=models.PROTECT)
    is_published = models.BooleanField()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-priority']

    def __str__(self):
        return self.playlist_title

