from django.urls import path
from . import views

app_name = 'notinator'
urlpatterns = [
    # ex: /polls/
    path('', views.homepage, name='homepage'),
    path('results/', views.results, name='results'),
    path('results/quiz/', views.quizpage, name='quizpage'),
    path('results/resoures/', views.resourespage, name='resourespage'),
]
