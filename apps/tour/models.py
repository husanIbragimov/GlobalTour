from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, Country


class Tour(BaseModel):
    name = models.CharField(max_length=225, verbose_name=_("Nomi"))
    slug = models.SlugField(max_length=225, unique=True, db_index=True, null=True, blank=True, verbose_name=_("Slug"))
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_("Shahar")
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Narxi"))
    duration = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Sayohat davomiyligi"))
    group = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Guruh"))
    description = RichTextField(null=True, blank=True, verbose_name=_("Tavsif"))

    class Meta:
        verbose_name = _('Sayohat')
        verbose_name_plural = _('Sayohatlar')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tour:tour_detail', kwargs={'slug': self.slug})


class TourPlan(BaseModel):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="plans",
        related_query_name="plan",
        verbose_name=_("Sayohat")
    )
    name = models.CharField(max_length=225, verbose_name=_("Nomi"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Tavsif"))

    class Meta:
        verbose_name = _('Sayohat reja')
        verbose_name_plural = _('Sayohat rejalar')

    def __str__(self):
        return self.name


class TourGallery(BaseModel):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="galleries",
        related_query_name="gallery",
        verbose_name=_("Sayohat")
    )
    image = models.ImageField(upload_to="galleries/", null=True, blank=True, verbose_name=_("Rasm"),
                              help_text=_("Rasm hajmi 1,200x1,700 px bo'lishi kerak. Havola: https://pexels.com/"))

    class Meta:
        verbose_name = _('Galereya')
        verbose_name_plural = _('Sayohat Galereyalari')

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
        related_query_name="booking",
        verbose_name=_("Sayohat")
    )
    status = models.IntegerField(choices=STATUS, default=0, verbose_name=_("Holat"))
    full_name = models.CharField(max_length=100, verbose_name=_("Ism Familiya"))
    phone_number = models.CharField(max_length=20, verbose_name=_("Telefon raqam"))
    people = models.PositiveIntegerField(default=1, verbose_name=_("Odamlar soni"))
    message = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Xabar"))
    date = models.DateField(null=True, blank=True, verbose_name=_("Sana"))

    class Meta:
        verbose_name = _('Buyurtma')
        verbose_name_plural = _('Buyurtmalar')

    def __str__(self):
        return self.full_name
