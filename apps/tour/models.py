from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, Country
from core.helper import latin_slugify


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
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.slug_ru or self.slag_ru != latin_slugify(self.name_ru):
            self.slug_ru = latin_slugify(self.name_ru)
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
        return self.image.url


class BookingTour(BaseModel):
    STATUS = (
        (0, _('New')),
        (1, _('Confirmed')),
        (2, _('Canceled')),
    )
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="bookings",
        related_query_name="booking"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    people = models.PositiveIntegerField(default=1)
    message = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name
