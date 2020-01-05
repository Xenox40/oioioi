from importlib import import_module

from django.conf import settings
import django.dispatch

# pylint: disable=unused-import
# Important. This import is to register signal handlers. Do not remove it.
import oioioi.base.signal_handlers
from oioioi.base.utils import is_internal_app_name
from oioioi.base.setup_check import setup_check

# Check if deployment and installation config versions match.
# Check if database settings are correct.
setup_check()

for app in settings.INSTALLED_APPS:
    if is_internal_app_name(app):
        try:
            # Controllers should be imported at startup, because they register
            # mixins
            import_module(app + '.controllers')
        except ImportError:
            pass

# Sender will be equal to the form that was completed
PreferencesSaved = django.dispatch.Signal()
