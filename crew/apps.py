from django.apps import AppConfig


class CrewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crew'

    def ready(self) -> None:
        import crew.signals