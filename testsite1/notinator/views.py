from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models

from .forms import InputForm
from .models import Quiz, ResourceList, QuizQuestion, Resource


def homepage(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['selection']
            if selection == '1':
                # subject = pr.getSubject(form.cleaned_data['text'])
                subject = 'null_subject'

                quiz_lists = Quiz.objects.filter(subject=subject)

                if len(quiz_lists) == 0 or form.cleaned_data['override_make_new']:
                    new_quiz = Quiz(subject=subject)
                    new_quiz.on_subject_index = len(quiz_lists)
                    new_quiz.name = 'Quiz for ' + subject
                    new_quiz.description = 'Quiz for ' + subject

                    new_quiz.questions = QuizQuestion(name='Question 1', body='Question 1')
                    new_quiz.questions.save();
                    # todo create question list using function calls to other code
                    new_quiz.save()

                else:
                    new_quiz = quiz_lists[0]

                return HttpResponseRedirect(reverse('notinator:quiz', args=(new_quiz.id,)))
            elif selection == '2':

                subject = 'null_subject'

                # checks if the resource list exists, and if not, creates it
                resource_lists: models.QuerySet = ResourceList.objects.filter(subject=subject)

                if len(resource_lists) == 0 or form.cleaned_data['override_make_new']:
                    new_resource = ResourceList(subject=subject)
                    new_resource.on_subject_index = len(resource_lists)
                    new_resource.name = 'Resources for ' + subject
                    new_resource.description = 'Resources for ' + subject

                    new_resource.resources = Resource(name='Resource 1', description='Resource 1')
                    new_resource.resources.save()

                    # todo create resource list using function calls to other code
                    new_resource.save()
                else:
                    new_resource = resource_lists[0]
                return HttpResponseRedirect(reverse('notinator:resources', args=(new_resource.id,)))
            else:
                return HttpResponseRedirect(reverse('notinator:homepage'), {'form': form})

    else:
        form = InputForm()

    return render(request, 'notinator/homepage.html', {'form': form})


def quiz(request, quiz_id):
    quiz1 = get_object_or_404(pk=quiz_id, klass=Quiz.objects.all())

    return render(request, 'notinator/quizpage.html',
                  context={'quiz': quiz1})


def resources(request, resource_list_id):
    resource_list = get_object_or_404(pk=resource_list_id, klass=ResourceList.objects.all())

    return render(request, 'notinator/resourcepage.html',
                  context={'resource_list': resource_list})


# Create your views here.
def results(request):
    return homepage(request)
