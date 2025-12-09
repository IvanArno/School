from django.contrib import admin
from .models import Poster, Performance, Photo, Category

@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'created_at']
    list_filter = ['date']

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'has_video', 'created_at']
    list_filter = ['date']
    
    def has_video(self, obj):
        return bool(obj.video_url or obj.video_file)
    has_video.boolean = True
    has_video.short_description = 'Есть видео'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploaded_at']
    list_filter = ['category']