import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils import simplejson

class RssInput(models.Model):
	address = models.CharField(max_length=150)
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	
	def get_absolute_url(self):
		return reverse('rssinput_list', kwargs={'pk': self.pk})
	
	def __str__(self):
		return 'ID: '+str(self.id)+', NASLOV:'+self.title+', URL:'+self.address

class FeedManager(models.Manager):
	def all_categories(self):
		from django.db import connection
		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT(category)
			FROM rss_rssfeedbulk
			""")
		result_list = []
		for row in cursor.fetchall():
			f = row[0]
			result_list.append(f)
		return result_list
	
	def all_authors(self):
		from django.db import connection
		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT(author)
			FROM rss_rssfeedbulk
			""")
		result_list = []
		for row in cursor.fetchall():
			f = row[0]
			result_list.append(f)
		return result_list
		
class RssFeedBulk(models.Model):
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	href = models.CharField(max_length=350)
	author = models.CharField(max_length=150)
	img_src = models.CharField(max_length=350)
	category = models.CharField(max_length=150)
	#author_link_id = models.ForeignKey('Author', null=True)
	#slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
	objects = FeedManager()
	
	
	#def get_absolute_url(self):
	#	return reverse('rsscategory_list', kwargs={'category': self.category})
	
	def __str__(self):
		return 'id: %s title: %s date: %s link: %s author: %s img link: %s category %s ' % (self.id, self.title, self.pub_date, self.href, self.author, self.img_src, self.category)

class Author(models.Model):
	author_name = models.ForeignKey('rss.rssfeedbulk')
