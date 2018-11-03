from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.entry),
    url(r'^enter$', views.enter),
    url(r'^reset$', views.reset)
] 