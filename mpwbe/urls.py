"""mpwbe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings #
from django.conf.urls.static import static #
from pages.views import login_view , contact_view , politics_view , news_create_view

urlpatterns = [
    
    path('', include('static_pages.urls')),
    path('news/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('login/', login_view , name='login'),
    path('contact/', contact_view , name = 'contact'),
    path('politics/', politics_view , name='politics'),
    path('newscreate/', news_create_view ),
    
    ]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
