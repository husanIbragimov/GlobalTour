from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, Country


class Tour(BaseModel):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Narxi"))
    duration = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Sayohat davomiyligi"))
    group = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Guruh"))
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f"{self.name}".replace(' ', '-').lower().replace('.', '')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tour:tour_detail', kwargs={'slug': self.slug})


class TourPlan(BaseModel):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="plans",
        related_query_name="plan"
    )
    name = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TourGallery(BaseModel):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="galleries",
        related_query_name="gallery"
    )
    image = models.ImageField(upload_to="galleries/", null=True, blank=True)

    def __str__(self):
        return self.tour
