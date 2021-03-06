from django import forms
from .models import Quiz, QuizQuestion
from django.utils.safestring import mark_safe


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
    def __init__(self, quiz_arg: Quiz, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.quiz = quiz_arg

        # assert form_quiz_object.questions is list[Quiz.QuizQuestion]
        for i, question in enumerate(QuizQuestion.objects.filter(quiz=self.quiz)):

            if question.base_question:
                # Base question
                self.fields[question.name] = forms.CharField(
                    label=mark_safe('Question: ' + str(i) + '<br />' + question.name + '<br />' + question.body),
                    max_length=200,
                    initial='enter your answer here',
                    required=True)

            if question.multiple_choice_question:
                # this is for multiple choice, support for other types will be added later
                self.fields[question.name] = \
                    forms.ChoiceField(
                        choices=question.choices,
                        label=mark_safe('Question: ' + str(i) + '<br />' + question.name + '<br />' + question.body),
                        required=True)

    def mark(self):
        print("test success")

        question: QuizQuestion
        for i, question in enumerate(QuizQuestion.objects.filter(quiz=self.quiz)):
            print("test success2")

            answer = self.cleaned_data[question.name]

            if question.multiple_choice_question:
                # this is for multiple choice, support for other types will be added later
                answer = self.cleaned_data[question.name]

            self.fields[question.name].required = False
            label = self.fields[question.name].label
            self.fields[question.name].label = \
                mark_safe("Question: {} <br /> Your answer: {} <br /> Feedback: {}".format(
                    label, answer, question.get_feedback(answer)))
