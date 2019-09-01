from django.shortcuts import render , get_object_or_404
# Create your views here.
from django.views.generic import ListView, DetailView #, CreateView
from django.views.generic.edit import CreateView
from .models import PreNews
from .forms import PreNewsForm

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
	template_name = 'create/newscreate.html'
	fields = [ 'author' , 'title' , 'main_pic' , 'choice', 'brief', 'article', 'slug', 'tags' ]
	
	
	# ~ def form_valid(self, form):
		# ~ #print(form.cleaned_data)
		# ~ return super().form_valid(form)
	
