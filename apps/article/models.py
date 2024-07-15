from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse

from django.template.defaultfilters import slugify

from apps.common.models import BaseModel


class Article(BaseModel):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'slug': self.slug})


class Comment(BaseModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment'
    )
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        limit_choices_to={'parent__isnull': True}
    )
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
