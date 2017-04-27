# myproject/settings.py
# -*- coding: UTF-8 -*-
from conf.base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mybus',
        'USER': 'odoo',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# settings.py
# … put this at the end of the file …
#try:
#    execfile(os.path.join(os.path.dirname(__file__), "local_settings.py"))
#except IOError:
#    pass
