from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.post_list, name="list"),
    url(r'^11$', views.post_list_11, name="list_11"),
    url(r'^12$', views.post_list_12, name="list_12"),
    url(r'^13$', views.post_list_13, name="list_13"),
    url(r'^plus$', views.post_list_plus, name="list_plus"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^P<slug>[\w-]+/$', views.post_detail, name="detail"),
]
