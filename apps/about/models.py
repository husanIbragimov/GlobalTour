from ckeditor.fields import RichTextField
from django.db import models

from apps.common.models import BaseModel


class About(BaseModel):
    name = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', null=True, blank=True)

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
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=TYPES)
    url = models.URLField(default='#')

    def __str__(self):
        return self.name
