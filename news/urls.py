from django.urls import path
from .views import (NewsListView , NewsDetailView , 
					#NewsCreateT, 
					NewsCreateView , 
					NewsUpdateView , NewsDeleteView)
#app_name = 'news' ##
urlpatterns = [ 
	
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete', NewsDeleteView.as_view(), name='sub_news_delete'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/', NewsUpdateView.as_view(), name='sub_news_edit'),
	path('create/', NewsCreateView.as_view(), name='news_create'),
	#path('salam/', NewsCreateT.as_view() ,name='news_test'),
	path('<int:year>/<int:month>/<int:day>/<slug:slug>/', NewsDetailView.as_view(), name='sub_news_url'),
	path('', NewsListView.as_view(), name='news'),
	 ] 
