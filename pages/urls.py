from django.urls import path
from .views import ContactView


urlpatterns = [

    # ~ path('news/', NewsView.as_view(),name='News-View'),
    # ~ path('news/<int:year>_<int:month>_<int:day>_<int:id>/' ,NewsSubView.as_view() , name='sub_news_url_name'),
    path("", ContactView.as_view(),name='contact')
    
]
