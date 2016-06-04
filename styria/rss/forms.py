from django import forms
#from django.core.urlresolvers import reverse
#from django.http import HttpResponseForbidden
#from django.views.generic import FormView
#from django.views.generic.detail import SingleObjectMixin

#from .models import RssInput

#class RssForm(forms.Form):

#class RssBasic(SingleObjectMixin, FormView):
class RssBasicForm(forms.Form):
    rss_address = forms.CharField(label='Rss address', max_length=255)
    rss_title = forms.CharField(label='Rss title', max_length=255)
