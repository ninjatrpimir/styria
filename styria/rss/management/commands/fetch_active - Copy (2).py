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
	
	def handle(self, *args, **options):
	
		self.list = []
		xml='http://www.24sata.hr/feeds/aktualno.xml'
		self.root = etree.parse(xml, base_url='http://www.24sata.hr/feeds/aktualno.xml')
		
		#for self.r in tree.xpath('//description'):
			#href = element.items()[0][1]  #gives you the value corresponding to the key "href"
			#src = element.xpath('//img/@src')[0]
			#print(src)
		
		for self.r in self.root.iter('item'):			
			#if (self.r.findtext('title') != None):
				#self.title = item.findtext('title')
				#self.list.append(self.r.findtext('title'))
			#if (self.r.findtext('link') != None):
				#self.list.append(self.r.findtext('link'))
				#self.list.append(self.link)
			if (self.r.findtext('description') != None):
				soup = BeautifulSoup(self.r.findtext('description'))
				page_pages = [image["src"] for image in soup.findAll("img")]
				print(page_pages)
				
				"""
				for link in self.root.xpath('description//img'):
					print('lol')
					img = link.find('img')
					print (img.get(src))
				"""
				#img = self.r.findtext('description')
				#img = self.root.get('//img/@src')
				#self.root.xpath('//img/@src')
				#self.list.append(img)
				#self.list.append(self.r.findtext('description'))
				#self.list.append(self.description)
			if (self.r.findtext('pubDate') != 'None'):
				self.list.append(self.r.findtext('pubDate'))
			#	self.list.append(self.pubDate)
			if (self.r.findtext('creator') != None):
				self.list.append(self.r.findtext('creator'))
				#self.list.append(self.author)
			#if (self.r.findtext('category') != None):
				#self.list.append(self.r.findtext('category'))
				#self.list.append(self.category)
			
			print (self.list)
			
			"""
			self.title = item.findtext('title')
			self.link = item.findtext('link')
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
		"""