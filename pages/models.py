from django.db import models
from django.urls import reverse

# Create your models here.

class LoginFormModel(models.Model):
	
	username = models.CharField(max_length=32)
	email 	 = models.EmailField()
	password = models.CharField(max_length=32)
	def __str__(self):
		return self.username

class NewsModel(models.Model):
	
	title		= models.CharField(max_length=80,null=False,blank=False)
	author		= models.CharField(max_length=32,null=False,blank=False)
	date		= models.DateTimeField(auto_now_add=True)
	news_pic	= models.ImageField(null=True,blank=True,upload_to='images/')
	news_par	= models.TextField(max_length=10000)
	news_long_par	= models.TextField(max_length=100000,null=True,blank=True)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("news:sub_news_url_name", kwargs = {'id' : self.id , 'year' : self.date.year , 'month' : self.date.month , 'day' : self.date.day })
		

class ContactFormModel(models.Model):
	
	username = models.CharField(default="",max_length=32,null=False,blank=False)
	comment	 = models.TextField(max_length=1000,null=False,blank=False)
	date     = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return (self.username,self.comment)
