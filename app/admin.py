from django.contrib import admin

from .models import *

admin.site.register(PayUser)
admin.site.register(Expense)
admin.site.register(Merchant)
admin.site.register(Approval)
