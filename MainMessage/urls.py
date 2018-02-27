from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^type_list/$', views.type_list),
    url(r'^type_mesage/$', views.list),
    url(r'^service_type/$', views.service_list),
    url(r'^service_detail_type/$', views.service_detail_list),
    url(r'^service_message/$', views.service_message),
]
