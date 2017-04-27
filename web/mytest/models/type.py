# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Type(models.Model):
    title = models.CharField(max_length=200)
    state = models.SmallIntegerField()

    class Meta:
        app_label = 'mytest'
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __str__(self):
        return self.title
