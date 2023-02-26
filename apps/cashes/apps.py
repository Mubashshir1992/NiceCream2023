from django.apps import AppConfig


class CashesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cashes'

    def ready(self):
        import apps.cashes.signals
