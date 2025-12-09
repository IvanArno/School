from django.contrib import admin
from .models import Poster, Performance, Photo, Category

@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'created_at']

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploaded_at']