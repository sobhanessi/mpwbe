from django.db import models
from pages.models import LoginFormModel
from django.urls import reverse
# Create your models here.

class PreNews(models.Model):
	
	author = models.ForeignKey('pages.LoginFormModel', on_delete = models.CASCADE ,)
	title = models.TextField(max_length=100,null=False)
	slug = models.SlugField(unique=True)
	date = models.DateTimeField(auto_now_add=True)
	main_pic = models.ImageField(upload_to='images/',null=False)
	brief = models.TextField(max_length=255,null=False)
	article = models.TextField(null=False)
	
	def get_absolute_url(self):
		return reverse('news:sub_news_url', kwargs = { 'slug' : self.slug ,'year' : self.date.year , 'month' : self.date.month , 'day' : self.date.day })
		
