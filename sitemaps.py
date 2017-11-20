from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from splash_page.urls import urlpatterns 

class StaticSitemap(Sitemap):
	priority = 0.8
	changefreq = 'weekly'

	# Return all urls defined in urls.py file
	def items(self):
		return ['home',]

	def location(self, item):
		return reverse(item)

