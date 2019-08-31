from django.db import models
from pages.models import LoginFormModel
from django.urls import reverse
# Create your models here.

class PreNews(models.Model):
	
	hardware = 'chw'
	software = 'csw'
	politics_iran = 'pir'
	politics_international = 'pin'
	news_choice = [
		(hardware,'computer hardware news'),
		(software,'computer software news'),
		(politics_iran,'iran politics'),
		(politics_international,'international politics'),
			]
	
	author = models.ForeignKey('pages.LoginFormModel', on_delete = models.CASCADE ,)
	title = models.TextField(max_length=100,null=False)
	tags = models.TextField(default='sobhan esfandyari,')
	choice = models.CharField(max_length=3 , choices=news_choice , default=software)
	slug = models.SlugField(unique=True,blank=False,null=False)
	date = models.DateTimeField(auto_now_add=True)
	main_pic = models.ImageField(upload_to='images/',null=False)
	brief = models.TextField(max_length=255,null=False)
	article = models.TextField(null=False)
	
	def __str__(self):
		return (self.title," ---- ",self.date.year ,"-",self.date.month,"-" ,self.date.day," ---- " ,self.date.hour ,":", self.date.minute," ---- ",self.author)
	def get_absolute_url(self):
		return reverse('sub_news_url', kwargs = { 'slug' : self.slug ,'year' : self.date.year , 'month' : self.date.month , 'day' : self.date.day })
		
