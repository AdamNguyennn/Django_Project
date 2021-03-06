from os import name
from django.urls import path 
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('count', views.count, name='count'),
	path('post/<str:sth>', views.post, name='post'),
]