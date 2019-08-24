from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^home/$',views.picassoHome,name='picassoHome'),
    url(r'^search/$',views.search_results,name='search_results')
]