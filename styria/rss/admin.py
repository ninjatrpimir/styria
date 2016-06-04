from django.contrib import admin

from .models import RssInput, RssFeedBulk

admin.site.register(RssInput)
admin.site.register(RssFeedBulk)

# Register your models here.
