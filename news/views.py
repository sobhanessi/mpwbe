from django.shortcuts import render , get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
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
	#fields = [ 'author' , 'title' , 'main_pic' , 'choice', 'brief', 'article', 'slug', 'tags' ]
	fields = '__all__'
	#form_class = PreNewsForm
	template_name = 'create/newscreate.html'
	
	def form_valid(self, form):
		
		model = form.save(commit=False)
		model.author = self.request.user
		model.save()
		
		return HttpResponse('naridi khodaro shokr')
		
	def get_success_url(self):
		
		return reverse('sub_news_url')
		#print(self.request.user)
		# ~ self.object = form.save(commit=False)
		# ~ self.object.author = self.request.author
		# ~ self.object.save()
		# ~ form.instance.author = self.request.author
		# ~ form.instance.date = datetime.now()
		# ~ form.instance.save()
		# ~ #return super(NewsCreateView, self).form_valid(form)
	
	# ~ def form_valid(self, form):
		# ~ #print(form.cleaned_data)
		# ~ return super().form_valid(form)
	
