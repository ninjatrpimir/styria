from django.core.management.base import BaseCommand, CommandError
from django.http import HttpResponse
from bs4 import BeautifulSoup

from urllib.request import urlopen
import xml.etree.ElementTree
from xml.etree.ElementTree import parse
from lxml import etree, objectify
from io import StringIO, BytesIO
#from xml.etree.ElementTree import iterparse
#from xml.etree.ElementTree import iterchildren

from rss.models import RssInput, RssFeedBulk


"""
http://lxml.de/tutorial.html
http://stackoverflow.com/questions/33225181/valueerror-can-only-parse-strings-python
"""

class Command(BaseCommand):
	help = 'Fetches active feeds'
	
	#def add_arguments(self, parser):
	#	parser.add_argument('id', nargs='+', type=int)
	"""	
	def iterchidren(self, 'item'):
		self.channel = etree.Element("channel")
		u = urlopen('http://www.24sata.hr/feeds/aktualno.xml')
		doc = parse(u)
	"""
	def handle(self, *args, **options):
		xml='http://www.24sata.hr/feeds/aktualno.xml'
		self.root = etree.parse(xml, base_url='http://www.24sata.hr/feeds/aktualno.xml')
		#print(self.root)
		"""
		for p in self.root.findall('item'):
			for r in p.iter():
				title = item.findtext('title')
				print (title)
		"""
		for r in self.root.iter('item'):
			title = r.findtext('title')
			print (title)
		#self.tree = etree.tostring(self.root)
		#self.tree = etree.parse(self.root)
		#self.tree = etree.tostring(self.tree)
		#self.tree = etree.parse(StringIO(self.tree))
		#self.tree = etree.objectify.fromstring(self.tree)
		#print (self.tree)
		# Download the RSS feed and parse it
		#u = urlopen('http://www.24sata.hr/feeds/aktualno.xml')
		#self.doc = parse(u)
		#print (self.tree)
		#self.list = []
		"""
		#self.root = etree.Element('channel')
		# Extract and output tags of interest
		#child.tag for child in self.channel.iterchildren():
			
			
			self.item = item.findtext('item')
			self.title = item.findtext('title')
			self.link = item.fi#ndtext('link')
			self.description = item.findtext('description')
			self.pubDate = item.findtext('pubDate')
			self.author = item.findtext('dc:creator')
			self.category = item.findtext('category')
				
			if (item.findtext('item:title') != None):
				self.title = item.findtext('title')
				self.list.append(self.title)
			if (item.findtext('link') != None):
				self.link = item.findtext('link')
				self.list.append(self.link)
			if (item.findtext('description') != None):
				self.description = item.findtext('description')
				self.list.append(self.description)
			#if (self.pubDate != 'None'):
			#	self.list.append(self.pubDate)
			if (item.findtext('author') != None):
				self.author = item.findtext('author')
				self.list.append(self.author)
			if (item.findtext('category') != None):
				self.category = item.findtext('category')
				self.list.append(self.category)
		"""
			
		#print(self.list)
			#form = RssForm
            #cd = form.cleaned_data
            #r = RssInput(address=cd['address'],
            #            title=cd['title'])
            #r.save()
			#spremiti u listu
			#print(title)
			#print(link)
			#print(description)
			#print(pubDate)
			#print(author)
			#print(category)