from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	
	username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
	email	 = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
	age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
	
	class Meta:
		
		model = CustomUser
		fields = ('username' , 'email', 'age')
		
		
class CustomUserChangeForm(UserChangeForm):
	
	username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
	email	 = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
	
	class Meta:
		
		model = CustomUser
		fields = ('username', 'email' , 'age' )
		

