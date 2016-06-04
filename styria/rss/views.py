from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.generic import View, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic.edit import FormView


from .models import RssInput, RssFeedBulk
from .forms import RssBasicForm

class RssListInput(View):
	def get(self, request, *args, **kwargs):
		view = RssList.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = RssBasic.as_view()
		return view(request, *args, **kwargs)

class RssList(ListView):
	model = RssInput	
	
	def get_context_data(self, **kwargs):
		context = super(RssList, self).get_context_data(**kwargs)
		form = RssBasicForm
		context['form'] = form
		return context
		
class RssDelete():
	model = RssInput

#postavi post u glavni class
class RssBasic(FormView, SingleObjectMixin):
	template_name = 'rss/rssinput_list.html'
	form_class = RssBasicForm
	model = RssInput
	
	def post(self, request, *args, **kwargs):
		
		form = RssBasicForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			r = RssInput(address=cd['rss_address'],
						 title=cd['rss_title'])
			r.save()
			
			return HttpResponseRedirect('list')

class RssEntry(ListView):
	model = RssFeedBulk
	template_name = 'rss/rssfeedbulk_list.html'
	paginate_by = 20
	
	def get_context_data(self, **kwargs):
		context = super(RssEntry, self).get_context_data(**kwargs) 
		rssfeedbulk_list_earliest = RssFeedBulk.objects.order_by('-pub_date')
		paginator = Paginator(rssfeedbulk_list_earliest, self.paginate_by)

		page = self.request.GET.get('page')

		try:
			rssfeedbulk_list_earliest = paginator.page(page)
		except PageNotAnInteger:
			rssfeedbulk_list_earliest = paginator.page(1)
		except EmptyPage:
			rssfeedbulk_list_earliest = paginator.page(paginator.num_pages)

		context['rssfeedbulk_list_earliest'] = rssfeedbulk_list_earliest
		return context
		
class RssCategory(ListView):
	model = RssFeedBulk
	template_name = 'rss/rsscategory_list.html'
	paginate_by = 20
	
	
	def get_context_data(self, **kwargs):
		context = super(RssCategory, self).get_context_data(**kwargs)
		#self.category = self.request.GET.get('category')
		#category = self.category
		#rss_category_list = RssFeedBulk.objects.filter(category=self.category)
		rss_category_list = RssFeedBulk.objects.filter(category='Tech')
		paginator = Paginator(rss_category_list, self.paginate_by)

		page = self.request.GET.get('page')

		try:
			rss_category_list = paginator.page(page)
		except PageNotAnInteger:
			rss_category_list = paginator.page(1)
		except EmptyPage:
			rss_category_list = paginator.page(paginator.num_pages)

		rss_all_categories = RssFeedBulk.objects.all_categories() 
		context['rss_category_list'] = rss_category_list
		context['rss_all_categories'] = rss_all_categories
		return context
	
"""	
def index(request):
    form = RssForm()
    rss_list = RssInput.objects.order_by('title')
    context = {'rss_list': rss_list, 'form': form}
    return render(request, 'rss/index.html', context)

def rss_save(request):
    if request.method == 'POST':
        form = RssForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            r = RssInput(address=cd['address'],
                         title=cd['title'])
            r.save()
            
            return HttpResponseRedirect('rss/index.html')
"""
    # if a GET (or any other method) we'll create a blank form
    #else:
    #    form = RssForm()

    #return render(request, 'name.html', {'form': form})
