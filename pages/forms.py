from django import forms
from .models import LoginFormModel,ContactFormModel,NewsModel

class NewsCreateForm(forms.ModelForm):
	class Meta:
		model = NewsModel
		fields = ['title','author','news_pic','news_long_par','news_par']

class LoginForm(forms.Form):
	
	username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
	email	 = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

class ContactForm(forms.ModelForm):
	

	class Meta:
		model = ContactFormModel
		fields = '__all__'
		
		
