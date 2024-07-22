from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from django.utils.translation import gettext as _

from apps.common.models import BaseModel
from core.helper import latin_slugify


class Article(BaseModel):
    name = models.CharField(max_length=225, verbose_name=_("Nomi"))
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True, verbose_name=_("Slug"))
    content = RichTextField(null=True, blank=True, verbose_name=_("Tavsif"))
    image = models.ImageField(upload_to='article/', null=True, blank=True, verbose_name=_("Rasm"))

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.slug_ru or self.slag_ru != latin_slugify(self.name_ru):
            self.slug_ru = latin_slugify(self.name_ru)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'slug': self.slug})


class Comment(BaseModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
        verbose_name=_("Maqola")
    )
    name = models.CharField(max_length=100, verbose_name=_("Ism"))
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        limit_choices_to={'parent__isnull': True},
        verbose_name=_("Parent")
    )
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Telefon raqam"))
    content = models.TextField(verbose_name=_("Matn"))
    is_published = models.BooleanField(default=False, verbose_name=_("Chop etilgan"))

    class Meta:
        verbose_name = 'Fikr'
        verbose_name_plural = 'Fikrlar'

    def __str__(self):
        return self.name
