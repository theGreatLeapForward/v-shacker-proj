from django.urls import path
from . import views

app_name = 'notinator'
urlpatterns = [
    # ex: /polls/
    path('', views.homepage, name='homepage'),
    path('results/', views.results, name='results'),
    path('results/quiz', views.quizresults, name='quizresults'),
    path('results/quiz/<int:quiz_id>/', views.quiz, name='quiz'),
    path('results/resoures/<int:resource_list_id>/', views.resources, name='resources'),
]
