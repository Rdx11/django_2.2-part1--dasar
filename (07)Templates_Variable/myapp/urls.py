from django.urls import path

from . import views

urlpatterns = [
	path('story/',views.story),
	path('news/',views.news),
	path('', views.index),
]