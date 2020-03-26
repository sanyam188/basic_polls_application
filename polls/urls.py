from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sj/', views.index2, name='index2'),
    path('sj/sj', views.index22, name='index2'),
]