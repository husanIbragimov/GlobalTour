from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
