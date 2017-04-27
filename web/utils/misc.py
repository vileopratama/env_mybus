# -*- coding: utf-8 -*-
# utils/misc.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


def custom_show_toolbar(request):
    return "1" == request.COOKIES.get("DebugToolbar", False)
