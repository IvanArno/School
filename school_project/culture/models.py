from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Poster(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posters/')
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Performance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    
    # Видео поля
    video_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Ссылка на видео YouTube/Vimeo (если есть)"
    )
    video_file = models.FileField(
        upload_to='videos/', 
        blank=True, 
        null=True,
        help_text="Или загрузите видеофайл"
    )
    video_caption = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def get_video_type(self):
        """Определяем тип видео"""
        if self.video_url:
            if 'youtube.com' in self.video_url or 'youtu.be' in self.video_url:
                return 'youtube'
            elif 'vimeo.com' in self.video_url:
                return 'vimeo'
            return 'external'
        elif self.video_file:
            return 'uploaded'
        return None

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title