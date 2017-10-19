from django.conf.urls import url

from . import views

# Url for the home page

urlpatterns = [
	
	# home page
	url(r'^$', views.home, name='home'),

	]