from django.apps import AppConfig


class TriggerConfig(AppConfig):
    name = 'trigger'

    def ready(self):
        import trigger.utils