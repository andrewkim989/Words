from django.conf.urls import url, include  

urlpatterns = [
    url(r'^', include('apps.s_words.urls')) 
]