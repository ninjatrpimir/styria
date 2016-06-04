from django.core.management.base import BaseCommand, CommandError
from django.http import HttpResponse
#import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

#import xml.etree as etree
from urllib.request import urlopen
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import iterparse

#import xmltodict DEPRECATED
from rss.models import RssInput, RssFeedBulk
#from xml.dom.minidom import parse
#import xml.dom.minidom


class Command(BaseCommand):
	help = 'Fetches active feeds'
	
	#def add_arguments(self, parser):
	#	parser.add_argument('id', nargs='+', type=int)
		
	def handle(self, *args, **options):
		# Download the RSS feed and parse it
		u = urlopen('http://www.24sata.hr/feeds/aktualno.xml')
		doc = parse(u)

		# Extract and output tags of interest
		for item in doc.iter():
			#item = item.findtext('item')
			title = item.findtext('title')
			link = item.findtext('link')
			description = item.findtext('description')
			pubDate = item.findtext('pubDate')
			author = item.findtext('dc:creator')
			category = item.findtext('category')
			
		#.iterfind('channel/item'):
			#title = item.findtext('title')
			#date = item.findtext('pubDate')
			#link = item.findtext('link')

			#print(item)
			#spremiti u listu
			print(title)
			print(link)
			print(description)
			print(pubDate)
			print(author)
			print(category)
			#print(date)
		#print(doc)
			
	
		#element =  ET.XML('http://www.24sata.hr/feeds/aktualno.xml')
		#url = 'http://www.24sata.hr/feeds/aktualno.xml'
		#parser = etree.XMLParser(recover=True)
		#tree = etree.fromstring(url, parser=parser)
		#url = 'http://www.24sata.hr/feeds/aktualno.xml'
		#file = urllib2.urlopen('http://www.24sata.hr/feeds/aktualno.xml')
		#data = file.read()
		#file.close()
		#data = xmltodict.parse(data)
		
		#request = urllib2.Request('http://www.24sata.hr/feeds/aktualno.xml')
		#response = urllib2.urlopen(request)

    # set the body
		#r = HttpResponse(response.read())
		#print (r)
		#r.text
		#print (r)
		
		#html = urlopen("http://www.24sata.hr/feeds/aktualno.xml/")
		#html = HttpResponse(html.read())
		#with urllib.request.urlopen('http://www.24sata.hr/feeds/aktualno.xml/') as response:
		#	html = response.read()
		#DOMTree = xml.dom.minidom.parse('http://www.24sata.hr/feeds/aktualno.xml/')
		#collection = DOMTree.documentElement
		#print(collection)
		#ourl_str = 'http://www.24sata.hr/feeds/aktualno.xml/'
		#urllib.request.install_opener(opener)
		#xml = urllib.request.urlretrieve(url_str, )
		
		#f = urllib.request.urlopen(url_str, 'aktualno')

		#print (xml)
		#xml_str = urllib.request.urlretrieve(url_str)
		#xmldoc = urllib.parse(xml_str)
		#xmldoc = minidom.parseString(xml_str)

		#obs_values = xmldoc.getElementsByTagName('base:OBS_VALUE')
		# prints the first base:OBS_VALUE it finds
		#print (obs_values[0].firstChild.nodeValue)

		# prints the second base:OBS_VALUE it finds
		#print (obs_values[1].firstChild.nodeValue)

		# prints all base:OBS_VALUE in the XML doc
		#for obs_val in obs_values:
		#	print (obs_val.firstChild.nodeValue)
		
		
		