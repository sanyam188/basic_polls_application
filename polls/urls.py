from django.urls import path

from . import views
app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('sj/', views.index2, name='index2'),
    path('sj/sj', views.index22, name='index2'),
    path('<int:q_id>/', views.detail,name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]