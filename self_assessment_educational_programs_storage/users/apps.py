from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "self_assessment_educational_programs_storage.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import self_assessment_educational_programs_storage.users.signals  # noqa F401
        except ImportError:
            pass
