from django.contrib import admin
from .models import PreNews2 , Comment
# Register your models here.



class CommentInline(admin.TabularInline):
	
	model = Comment

class PreNews2Admin(admin.ModelAdmin):
	
	inlines = [ CommentInline, ]


admin.site.register(PreNews2, PreNews2Admin)
admin.site.register(Comment)
