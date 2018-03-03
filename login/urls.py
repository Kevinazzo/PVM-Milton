from django.urls import path
from django.conf.urls import url
import login.views 


urlpatterns=[
	path(r'^(?P<usuario>\w{0,50})\%(?P<password>\w{0,32})', login.views.login),
	path(r'^hola/(?P<id>\d)',login.views.hola)
]