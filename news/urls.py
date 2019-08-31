from django.urls import path
from .views import NewsListView , NewsDetailView
#app_name = 'news' ####
urlpatterns = [ 
	
	path('', NewsListView.as_view(), name='news'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/', NewsDetailView.as_view(), name='sub_news_url'),
	
	
	 ] 
