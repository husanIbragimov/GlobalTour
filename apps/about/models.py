from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel


class About(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Nomi'))
    description = RichTextField(null=True, blank=True, verbose_name=_('Tavsif'))
    image = models.ImageField(upload_to='about/', null=True, blank=True, verbose_name=_('Rasm'),
                              help_text=_('Rasm hajmi 1200x1700 px bo\'lishi kerak. Havola: https://pexels.com/'))
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Telefon raqam'))

    class Meta:
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'

    def __str__(self):
        return self.name


class Team(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Ism Familya'))
    image = models.ImageField(upload_to='team/', null=True, blank=True, verbose_name=_('Rasm'),
                              help_text=_('Rasm hajmi 650X800 px bo\'lishi kerak. Havola: https://pexels.com/'))

    class Meta:
        verbose_name = 'Jamoa a\'zosi'
        verbose_name_plural = 'Jamoa a\'zolari'

    def __str__(self):
        return self.name


class SocialLink(BaseModel):
    TYPES = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('linkedin', 'Linkedin'),
        ('youtube', 'Youtube'),
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='social_links',
                             related_query_name='social_link', verbose_name=_('Jamoa a\'zosi'))
    name = models.CharField(max_length=100, choices=TYPES, verbose_name=_('Tarmoq turi'))
    url = models.URLField(default='#', verbose_name=_('Havola'))

    class Meta:
        verbose_name = 'Ijtimoiy tarmoq havolasi'
        verbose_name_plural = 'Ijtimoiy tarmoq havolalari'

    def __str__(self):
        return self.name
