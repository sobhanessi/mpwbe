from django.shortcuts import render

# Create your views here.
from .models import CustomUser
from .forms import CustomUserChangeForm , CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
	
	form_class = CustomUserCreationForm
	template_name = 'registration/signup.html'
	success_url = reverse_lazy('home')
