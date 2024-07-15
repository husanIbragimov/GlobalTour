from django.db import models

from django.utils.safestring import mark_safe


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='countries/', null=True, blank=True)
    flag = models.ImageField(upload_to='flags/', null=True, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        limit_choices_to={'parent__isnull': True}
    )

    @property
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
