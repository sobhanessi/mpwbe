from django.shortcuts import render , redirect
from django.http import HttpResponse ,Http404
from django.shortcuts import get_object_or_404
from .forms import LoginForm, ContactForm , NewsCreateForm
from .models import LoginFormModel,NewsModel,ContactFormModel
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView


# ~ class NewsView(ListView):
	
	# ~ template_name = 'news/main_news.html'
	# ~ queryset 	  = NewsModel.objects.order_by('-date')
	
	

# ~ def news_create_view(request):
	
	# ~ my_form = NewsCreateForm
	# ~ if request.method == 'POST':
		# ~ my_form = NewsCreateForm(request.POST)
		# ~ if my_form.is_valid():
			# ~ usrn = request.POST.get('author')
			# ~ try:
				# ~ usr_chk = LoginFormModel.objects.get(username=usrn)
				# ~ news_create = NewsModel.objects.create(**my_form.cleaned_data)
			# ~ except:
				# ~ raise Http404
	# ~ my_context = {
		# ~ 'form': my_form
	# ~ }	
	# ~ return render(request,'create/newscreate.html',my_context)
	


def contact_view(request):
	#
	my_form = ContactForm(auto_id=False)
	if request.method == 'POST':
		my_form = ContactForm(request.POST, auto_id=False)
		if my_form.is_valid():
			usrn = request.POST.get('username')
			try:
				usr_login = LoginFormModel.objects.get(username=usrn)
				usr_msg   = ContactFormModel.objects.create(**my_form.cleaned_data)
				return HttpResponse('successful')
			except:
				raise Http404
	my_context = {
		'contact' : my_form
	}
	return render(request, 'contact/contact.html' , my_context)



def login_view(request):
	
	my_form = LoginForm(auto_id=False)
	
	if request.method == 'POST':
		my_form = LoginForm(request.POST , auto_id=False)
		if my_form.is_valid():
			try:
				user_login = LoginFormModel.objects.get(**my_form.cleaned_data)
				print(user_login)
				return HttpResponse('<h1> salam user </h1>')
			except:
				return HttpResponse('<h1> ridiiiii </h1>')
			
			
	return render(request,'login/login.html',{'form':my_form})

# ~ def news_main_view(request):
	
	# ~ news_m_v = NewsModel.objects.order_by('-date')
	# ~ my_context = {
		# ~ 'news': news_m_v
	# ~ }
	# ~ return render(request,'news/main_news.html',my_context)
	

# ~ class NewsSubView(DetailView):
	
	# ~ template_name = 'news/sub_news.html'
	# ~ model = NewsModel
	# ~ queryset = NewsModel.objects.all()
	
	# ~ def get_object(self):
		# ~ id_ = self.kwargs.get('id')
		# ~ print(id_)
		
		# ~ return get_object_or_404(NewsModel,id=id_)
		
		
		
		
# ~ def news_sub_view(request, year, month, day , my_id):
	
	# ~ try:
		# ~ news_s_v = NewsModel.objects.get(id=my_id)
	# ~ except NewsModel.DoestNotExist:
		# ~ raise Http404
	# ~ my_context = { 
		# ~ 'i' : news_s_v
		# ~ }
		
	# ~ return render(request,'news/sub_news.html',my_context)
	
def politics_view(request):
	
	return render(request, 'politics/politics.html' , {})


	

