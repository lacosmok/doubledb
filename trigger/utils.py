from django.db.models.signals import post_delete
from .models import ExampleModel
from django.dispatch import receiver


@receiver(post_delete, sender=ExampleModel)
def check_db(sender, instance, using, **kwargs):
    print("check bot db", instance, using)
