from django import forms

from .models import PreNews


class PreNewsForm(forms.ModelForm):
	
	class Meta:
		model = PreNews
		fields = [
			'author',
			'title',
			'main_pic',
			'article',
			'brief',
			'slug',
			'tags',
			'choice'
		
		]
