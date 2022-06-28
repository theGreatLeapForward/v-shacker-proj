from django import forms
from .models import Quiz


class InputForm(forms.Form):
    text = forms.CharField(
        label='Input',
        max_length=3000,
        initial='Enter your text and links here',
        required=True)

    selection = forms.ChoiceField(
        choices=(('1', 'Quiz'), ('2', 'Resources')),
        label='Choose a result',
        required=True)

    override_make_new = forms.BooleanField(
        label='Always create new result',
        required=False)


class QuizForm(forms.Form):
    def __init__(self, quiz: Quiz, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        form_quiz_object = quiz
        for question in form_quiz_object.questions:

            # this is for multiple choice, support for other types will be added later
            self.fields[question.name] = \
                forms.ChoiceField(
                choices=question.choices,
                label=question.body,
                required=True)

