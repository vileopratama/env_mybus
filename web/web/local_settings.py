# -*- coding: utf-8 -*-
# local_settings.py
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mybus',
        'USER': 'odoo',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [

    ],
    'SHOW_TOOLBAR_CALLBACK': "utils.misc.custom_show_toolbar",
    'SHOW_TEMPLATE_CONTEXT': True,
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEFAULT_WEBSITE_URL = "http:/localhost"
