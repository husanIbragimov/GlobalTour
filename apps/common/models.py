from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Nomi"))
    image = models.ImageField(upload_to='countries/', null=True, blank=True, verbose_name=_("Rasm"),
                              help_text=_("Rasm hajmi 1700x1133 px bo'lishi kerak. Havola: https://pexels.com/"))
    flag = models.ImageField(upload_to='flags/', null=True, blank=True, verbose_name=_("Bayroq"))
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        limit_choices_to={'parent__isnull': True},
        verbose_name=_("Parent")
    )

    @property
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    class Meta:
        verbose_name = "Shahar"
        verbose_name_plural = "Shaharlar"

    def __str__(self):
        return self.name
