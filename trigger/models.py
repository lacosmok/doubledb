from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255, default="")
    type = models.IntegerField(default=0)

    def double_save(self):
        self.save(using='seconddb')


class EventStart(models.Model):
    date = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
