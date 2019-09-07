from django import forms

from .models import PreNews2


class PreNewsForm(forms.ModelForm):
	
	class Meta:
		model = PreNews2
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
