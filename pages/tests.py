from django.test import TestCase
# Create your tests here.

from .models import NewsModel
from django.urls import reverse
from django.core.files import File
# ~ class NewsModelTest(TestCase):
	
	# ~ def setUp(self):
		
		# ~ NewsModel.objects.create(title='a django test', author='django',news_par='this is django self test')
		
	# ~ def test_text_content(self):
		
		# ~ post = NewsModel.objects.get(id=1)
		# ~ expected_object_name = f'{post.title}'
		# ~ self.assertEqual(expected_object_name,'a django test')

class NewsPageViewTest(TestCase):
	
	def setUp(self):
		
		NewsModel.objects.create(title='a django test 2', author='django' , news_par='nothing' , news_pic =File(file=b""))
		
	def test_view_url_exists_at_proper_location(self):
		
		resp = self.client.get('/news')
		self.assertEqual(resp.status_code,200)
		
	def test_view_url_by_name(self):
		
		resp = self.client.get(reverse('News-View'))
		self.assertEqual(resp.status_code,200)
		
	def test_view_uses_correct_template(self):
		
		resp = self.client.get(reverse('News-View'))
		self.assertEqual(resp.status_code,200)
		self.assertTemplateUsed(resp,'news/main_news.html')
