from django.apps import AppConfig


class BookshelfAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        import bookshelf.signals
