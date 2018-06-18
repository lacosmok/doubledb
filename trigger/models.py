from django.db import models
from django.utils import timezone


# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=255, default="")
    default_database = models.BooleanField(default=True)

    def double_save(self):
        self.save(using='seconddb')