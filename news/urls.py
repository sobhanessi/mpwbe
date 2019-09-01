from django.urls import path
from .views import NewsListView , NewsDetailView , NewsCreateView
app_name = 'news' ##
urlpatterns = [ 
	
	path('', NewsListView.as_view(), name='news'),
	path('create/', NewsCreateView.as_view(), name='news_create'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/', NewsDetailView.as_view(), name='sub_news_url'),
	
	
	 ] 
