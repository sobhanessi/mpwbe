from django.urls import path
from .views import AboutPageView , HomePageView

urlpatterns = [
	
	path('', HomePageView.as_view() , name = 'index'),
	path('aboutme/', AboutPageView.as_view(), name = 'aboutme'),
	
	]
