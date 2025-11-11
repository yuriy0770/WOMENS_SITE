from django.contrib import admin
from women.models import Category, Human

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'title', 'slug']
    list_filter = ['name']
    search_fields = ['name', 'title']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Human)
class AdminHuman(admin.ModelAdmin):
    list_display = ['name_h', 'cat', 'created_at']
    list_filter = ['cat', 'created_at']
    search_fields = ['name_h', 'descriptions']
    prepopulated_fields = {'slug': ('name_h',)}