from django.core.management.base import BaseCommand, CommandError
from django.http import HttpResponse
from bs4 import BeautifulSoup

from urllib.request import urlopen
import xml.etree.ElementTree
from xml.etree.ElementTree import parse
from lxml import etree, objectify
from datetime import datetime
import re

#from xml.etree.ElementTree import iterparse
#from xml.etree.ElementTree import iterchildren

from rss.models import RssInput, RssFeedBulk


"""
http://lxml.de/tutorial.html
"""

class Command(BaseCommand):
	help = 'Fetches active feeds'
	
	#dodaj path.xml kao argument za fetchanje feeda
	#python manage.py fetch_active sport 
	#def add_arguments(self, parser):
	#	parser.add_argument('id', nargs='+', type=int)
	
	def handle(self, *args, **options):
	
		self.list = []
		
		xml='http://www.24sata.hr/feeds/tech.xml'
		self.root = etree.parse(xml, base_url='http://www.24sata.hr/feeds/tech.xml')
			
		ns = { 'dc': 'http://purl.org/dc/elements/1.1/' }
		
		for self.r in self.root.iter('item'):
			if (self.r.findtext('title') != None):
				self.list.append(self.r.findtext('title'))
			if (self.r.findtext('link') != None):
				self.list.append(self.r.findtext('link'))
			if (self.r.findtext('description') != None):
				self.soup = BeautifulSoup(self.r.findtext('description'), 'lxml')
				self.img_src = [image["src"] for image in self.soup.findAll("img")]
				self.bchar = "[]'"
				for char in self.bchar:
					self.img_src = str(self.img_src).replace(char, '')
				self.list.append(self.img_src)
			if (self.r.findtext('pubDate') != None):
				self.pub_date = datetime.strptime(self.r.findtext('pubDate'), '%a, %d %b %Y %X %z').strftime('%Y-%m-%d %H:%M:%S')
				self.list.append(self.pub_date)
			if (self.r.find('dc:creator', ns).text != None):
				self.list.append(self.r.find('dc:creator', ns).text)
			if (self.r.findtext('category') != None):
				self.list.append(self.r.findtext('category'))
			
			f = RssFeedBulk(title = self.list[0],
							href = self.list[1],
							img_src = self.list[2],
							pub_date = self.list[3],
							authors = self.list[4],
							category = self.list[5])
			f.save()
			
			self.list[:] = []