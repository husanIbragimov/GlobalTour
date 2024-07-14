from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse

from apps.common.models import BaseModel


class Article(BaseModel):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f"{self.name}".replace(' ', '-').lower().replace('.', '')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'slug': self.slug})


class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.name
