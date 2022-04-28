from django.apps import AppConfig


class ShipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ship'
    
    def ready(self) -> None:
        import ship.signals
