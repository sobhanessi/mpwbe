from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	
	age = models.PositiveIntegerField(null=True,blank=True)
	# ~ username = models.CharField(max_length=32,unique=True,blank=False,null=False)
	# ~ email = models.EmailField(_('email address'), unique=True,
	
	# ~ USERNAME_FIELD = 'username'
	# ~ EMAIL_FIELD = 'email'
	# ~ REQUIRED_FIELDS = []
