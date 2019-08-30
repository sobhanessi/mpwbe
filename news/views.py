from django.shortcuts import render , get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import PreNews

class NewsListView(ListView):
	
	model = PreNews
	template_name = 'news/main_news.html'
	queryset = PreNews.objects.order_by('-date')

class NewsDetailView(DetailView):
	
	model = PreNews
	template_name = 'news/sub_news.html'
	#slug_url_kwarg = 'slug'
	
	def get_object(self):
		slug_ = self.kwargs.get('slug')
		return get_object_or_404(PreNews,slug=slug_)
		
