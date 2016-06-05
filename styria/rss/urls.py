from django.conf.urls import patterns, url, include
from rss.views import RssListInput
from rss.views import RssBasic
from rss.views import RssEntry
from rss.views import RssCategory
from dal import autocomplete
from rss.models import RssFeedBulk
from rss.views import AuthorAutocomplete

app_name = 'rss'
urlpatterns = [
	url(r'^author-ac$', autocomplete.Select2QuerySetView.as_view(model=RssFeedBulk),name='select2_fk'),
	url(r'^author-autocomplete$', AuthorAutocomplete.as_view(), name='author-autocomplete'),		
	url(r'^list-rss$', RssEntry.as_view()),
	url(r'^list-rss/category/(?P<category>[a-zA-Z]+)$', RssCategory.as_view(), name='rss-category'),
	url(r'^rec$', RssBasic.as_view()),
    url(r'^list$', RssListInput.as_view()),
]
