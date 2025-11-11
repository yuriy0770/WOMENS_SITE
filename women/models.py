from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Название категории')
    title = models.CharField(max_length=100, blank=True, verbose_name='Краткое описание')
    image_cat = models.ImageField(upload_to='category/', blank=True, verbose_name='Изображение категории')
    slug = models.SlugField(max_length=100, blank=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('women:category_detail', kwargs={'cat_slug': self.slug})


class Human(models.Model):
    name_h = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Имя')
    image = models.ImageField(upload_to='human/', blank=False, verbose_name='Фотография')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='humans', verbose_name='Категория')
    descriptions = models.TextField(blank=False, verbose_name='Описание')
    slug = models.SlugField(max_length=100, blank=True, verbose_name='URL')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_h)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_h

    def get_absolute_url(self):
        return reverse('women:human_detail', kwargs={'human_slug': self.slug})
