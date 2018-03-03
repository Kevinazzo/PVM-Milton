from django.urls import path,include
from pedidos import views as pedidosViews

urlpatterns=[
	path('/<int:id>', pedidosViews.consultaUsuario),
]