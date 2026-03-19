from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    # Enabled by default in Django 3.2+
    # default_auto_field = 'django.db.models.BigAutoField'

    name = 'apps.profiles'

    def ready(self):
        import apps.profiles.signals  # noqa
