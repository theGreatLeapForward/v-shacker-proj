from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import InputForm
from .models import Quiz, Resources


def homepage(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            selection = form.cleaned_data['selection']
            if selection == '1':
                return HttpResponseRedirect(reverse('notinator:quizpage'))
            elif selection == '2':
                return HttpResponseRedirect(reverse('notinator:resourespage'))
            else:
                return HttpResponseRedirect(reverse('notinator:homepage'))

    else:
        form = InputForm()

    return render(request, 'notinator/homepage.html', {'form': form})


def quizpage(request):
    return render(request, 'notinator/quizpage.html')


def resourespage(request):
    return render(request, 'notinator/resourcepage.html')


# Create your views here.
def results(request):
    return homepage(request)
