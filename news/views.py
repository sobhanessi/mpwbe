from django.shortcuts import render , get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView
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
		

class NewsCreateView(CreateView):
	
	model = PreNews
	template_name = 'create/news_create.html'
	fields = '__all__'
	#succes_url = '/news/'
	# ~ def get_object(self):
		# ~ slug_ = self.kwargs.get('slug')
		# ~ return get_object_or_404(PreNews,slug=slug_)
