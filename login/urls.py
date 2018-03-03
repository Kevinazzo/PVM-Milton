import views

urlpatterns=[
	path(r'^/(?P<username>\w{0,50})/$+(?P<password>\w{0,32}/$', login)
]