from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	
	form = UserChangeForm
	add_form = UserCreationForm
	model = CustomUser
	list_display = ['email' , 'username' , 'age' , 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
