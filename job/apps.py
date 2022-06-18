from django.apps import AppConfig


class JobSignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job'

    def ready(self):
        from . import signals
