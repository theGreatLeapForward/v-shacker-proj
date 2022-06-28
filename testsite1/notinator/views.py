from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models

from .forms import InputForm, QuizForm
from .models import Quiz, ResourceList, Resource, QuizQuestion


def homepage(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            selection: int = int(form.cleaned_data['selection'])

            if 0 < selection < 3:
                subject = 'null_subject'
                # todo: get subject from func call,

                # get a list of already-made resources
                resource_lists: models.QuerySet = ResourceList.objects.filter(subject=subject)

                # if there are no resources, create one
                if len(resource_lists) == 0 or form.cleaned_data['override_make_new']:
                    new_resource = ResourceList(subject=subject)
                    # todo: get resource body from function call
                    resource = Resource.objects.create()
                    resource.save()
                    new_resource.resources.set([resource])

                    new_resource.on_subject_index = len(resource_lists)
                    new_resource.save()
                else:
                    new_resource = resource_lists[0]

                # if the user requested a quiz, get that
                if selection == 1:
                    new_quiz = Quiz(subject=subject)

                    question = QuizQuestion.objects.create()
                    question.save()
                    new_quiz.questions.set([question])
                    # todo: get quiz from resource_list, and length from somewhere

                    # the length of the list of quizzes and corresponding resources should be the same
                    new_quiz.on_subject_index = len(resource_lists)
                    new_quiz.save()

                    # todo: store the dict of resource/quiz and indexes somewhere and use it
                    return HttpResponseRedirect(reverse('notinator:quiz', args=(new_quiz.id,)))

                return HttpResponseRedirect(reverse('notinator:resources', args=(new_resource.id,)))

            else:
                return HttpResponseRedirect(reverse('notinator:homepage'), {'form': form})

    else:
        form = InputForm()

    return render(request, 'notinator/homepage.html', {'form': form})


def quiz(request, quiz_id):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('notinator:quizresults', {'quiz_form': form}))

    selected_quiz = get_object_or_404(pk=quiz_id, klass=Quiz.objects.all())
    form = QuizForm(selected_quiz)

    return render(request, 'notinator/quizpage.html',
                  context={'form': form})


def resources(request, resource_list_id):
    resource_list = get_object_or_404(pk=resource_list_id, klass=ResourceList.objects.all())

    return render(request, 'notinator/resourcepage.html',
                  context={'resource_list': resource_list})


# Create your views here.
def results(request):
    return homepage(request)


def quizresults(request, quiz_form):
    return render(request, 'notinator/quizresults.html', context={'form': quiz_form})
