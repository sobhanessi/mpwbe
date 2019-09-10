from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render , get_object_or_404
from django.urls import reverse ,reverse_lazy
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView  
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import PreNews2 #, NewsCreateTM
from .forms import PreNewsForm

class NewsListView(ListView):
	
	model = PreNews2
	template_name = 'news/main_news.html'
	queryset = PreNews2.objects.order_by('-date')

class NewsDetailView(DetailView):
	
	model = PreNews2
	template_name = 'news/sub_news.html'
	#slug_url_kwarg = 'slug'
	
	def get_object(self):
		slug_ = self.kwargs.get('slug')
		return get_object_or_404(PreNews2,slug=slug_)
		

class NewsCreateView(LoginRequiredMixin , CreateView):

	model = PreNews2
	fields = '__all__'
	template_name = 'create/news_create.html'
	login_url = 'login'
	
	def form_valid(self, form):
	
		form.instance.author = self.request.user
		return super().form_valid(form)
			
	
class NewsUpdateView(LoginRequiredMixin , UpdateView):
	
	model = PreNews2
	template_name = 'create/news_create.html'
	fields = '__all__'
	login_url = 'login'
	
	def dispath(self,request, *args, **kwargs):
		
		obj = self.get_object()
		if obj.author != self.request.user :
			raise PermissionDenied
		return super().dispath(self,*args,**kwargs)

class NewsDeleteView(LoginRequiredMixin , DeleteView):
	
	model = PreNews2
	template_name = 'create/sub_news_delete.html'
	success_url = reverse_lazy('news')
	login_url = 'login'
		
	def dispath(self,request, *args, **kwargs):
		
		obj = self.get_object()
		if obj.author != self.request.user :
			raise PermissionDenied
		return super().dispath(self,*args,**kwargs)
