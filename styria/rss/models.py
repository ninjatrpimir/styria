import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

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
		
class RssFeedBulk(models.Model):
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	href = models.CharField(max_length=350)
	author = models.CharField(max_length=150)
	img_src = models.CharField(max_length=350)
	category = models.CharField(max_length=150)
	objects = FeedManager()
	
	def get_absolute_url(self):
		return reverse('rss_category_list', kwargs={'pk': self.pk})
	
	def __str__(self):
		return 'id: %s title: %s date: %s link: %s author: %s img link: %s category %s ' % (self.id, self.title, self.pub_date, self.href, self.author, self.img_src, self.category)

