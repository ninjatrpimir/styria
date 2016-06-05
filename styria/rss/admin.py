from django.contrib import admin

from .models import RssInput, RssFeedBulk, Author
#import autocomplete_light
#from dal import autocomplete

"""
class AuthorAdmin(admin.ModelAdmin):
	form = autocomplete.modelform_factory(Author)
"""
admin.site.register(RssInput)
admin.site.register(RssFeedBulk)
#admin.site.register(Author)
# Register your models here.
