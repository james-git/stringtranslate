from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'post_list/', views.post_list, name='post_list'),
	# url(r'^view_string_table/$', views.view_string_table, name='view_string_table'),
]
