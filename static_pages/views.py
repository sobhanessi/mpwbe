from django.shortcuts import render
from django.views.generic import TemplateView

class AboutPageView(TemplateView):
	
	template_name = 'aboutme/aboutme.html'

class HomePageView(TemplateView):
	
	template_name = 'index/index.html'

