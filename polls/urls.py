from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    #views.py에 있는 파라미터와 같아야하는 question_id
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]