from django.urls import path
from .views import NewsView, NewsSubView

app_name = 'news'
urlpatterns = [

    path('', NewsView.as_view(),name='News-View'),
    path('<int:year>_<int:month>_<int:day>_<int:id>/' ,NewsSubView.as_view() , name='sub_news_url_name'),
]
