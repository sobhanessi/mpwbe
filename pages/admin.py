from django.contrib import admin
from .models import NewsModel , LoginFormModel, ContactFormModel

# Register your models here.


admin.site.register(NewsModel)
admin.site.register(LoginFormModel)
admin.site.register(ContactFormModel)
