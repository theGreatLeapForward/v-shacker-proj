from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models

from .forms import InputForm, QuizForm
from .models import Quiz, ResourceList, QuizQuestion, Resource, QQMultipleChoice


def homepage(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            selection: int = int(form.cleaned_data['selection'])

            if 0 < selection < 3:
                subject = 'Addition'
                # todo: get subject from func call, as well as amount of resources/questions

                # get a list of already-made resources
                resource_lists: models.QuerySet = ResourceList.objects.filter(subject=subject)

                # if there are no resources, create one
                if len(resource_lists) == 0 or form.cleaned_data['override_make_new']:

                    # todo: get resource body from function call
                    new_resource = ResourceList(subject=subject, on_subject_index=len(resource_lists))
                    new_resource.save()

                    Resource(resource_list=new_resource, name='Wikipedia', description='',
                             r_link='https://en.wikipedia.org/wiki/Addition').save()
                    Resource(resource_list=new_resource, name='Cambridge', description='',
                             r_link='https://dictionary.cambridge.org/dictionary/english/addition').save()

                else:
                    new_resource = resource_lists[0]

                # if the user requested a quiz, get that
                if selection == 1:
                    # todo: get quiz from resource_list
                    quiz_lists: models.QuerySet = Quiz.objects.filter(subject=subject)

                    new_quiz = Quiz(subject=subject, on_subject_index=len(quiz_lists))
                    new_quiz.save()

                    QuizQuestion(quiz=new_quiz, name='What is addition?', body='').save()
                    choices1 = ['The Chinese', 'The Egyptians', 'The Babylonians', 'The Italians']
                    q = QQMultipleChoice(quiz=new_quiz, name='Who is credited with inventing addition?', body='',
                                         answer='')
                    q.choices = choices1
                    q.save()

                    # todo: store the dict of resource/quiz and indexes somewhere and use it
                    return HttpResponseRedirect(reverse('notinator:quiz', args=(new_quiz.id,)))

                return HttpResponseRedirect(reverse('notinator:resources', args=(new_resource.id,)))

            else:
                return HttpResponseRedirect(reverse('notinator:homepage'), {'form': form})

    else:
        form = InputForm()

    return render(request, 'notinator/homepage.html', {'form': form})


def quiz(request, quiz_id):
    selected_quiz = get_object_or_404(pk=quiz_id, klass=Quiz.objects.all())

    if request.method == 'POST':
        form = QuizForm(data=request.POST, quiz_arg=selected_quiz)
        if form.is_valid():
            form.mark()
            return render(request, 'notinator/quizresults.html', context={'form': form})
        else:
            return render(request, 'notinator/nosubmission.html')

    form = QuizForm(selected_quiz)

    return render(request, 'notinator/quizpage.html',
                  context={'form': form, 'path': ('/results/quiz/' + str(quiz_id) + '/')})


def resources(request, resource_list_id):
    resource_list = get_object_or_404(pk=resource_list_id, klass=ResourceList.objects.all())

    return render(request, 'notinator/resourcepage.html',
                  context={'resource_list': resource_list,
                           'resources': Resource.objects.filter(resource_list=resource_list)})


# Create your views here.
def results(request):
    return homepage(request)


""""{% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'notinator/style.css' %}">"""
