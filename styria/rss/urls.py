from django.conf.urls import patterns, url, include
from rss.views import RssListInput
from rss.views import RssBasic
from rss.views import RssEntry
from rss.views import RssCategory

app_name = 'rss'
urlpatterns = [
#	url(r'^autocomplete/', include('autocomplete_light.urls')),
	url(r'^category/(?P<category>[a-zA-Z]+)$', RssCategory.as_view()),
	url(r'^list-entry$', RssEntry.as_view()),
	url(r'^rec$', RssBasic.as_view()),
    url(r'^list$', RssListInput.as_view()),
]
