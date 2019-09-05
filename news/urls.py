from django.urls import path
from .views import NewsListView , NewsDetailView , NewsCreateT, NewsCreateView , NewsUpdateView
app_name = 'news' ##
urlpatterns = [ 
	
	path('', NewsListView.as_view(), name='news'),
	path('create/', NewsCreateView.as_view(), name='news_create'),
	path('salam/', NewsCreateT.as_view() ,name='news_test'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/', NewsUpdateView.as_view(), name='sub_news_edit'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/', NewsDetailView.as_view(), name='sub_news_url'),
	
	
	 ] 
