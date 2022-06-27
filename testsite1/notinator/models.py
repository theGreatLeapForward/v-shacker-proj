from django.db import models

from .forms import InputForm

# Create your models here.


class QuizQuestion(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    marked = False


class QQMultipleChoice(QuizQuestion):
    choices = list[models.CharField(max_length=200)]
    answer = models.CharField(max_length=200)


class Quiz(models.Model):
    """
    fields: quiz_subject, quiz_name, quiz_description,
        quiz_image, question_amount, questions, on_subject_index, misc_text
    methods: make_quiz
    """
    subject = models.CharField(max_length=100, default='null_subject')
    on_subject_index = models.IntegerField(default=0)

    name = models.CharField(max_length=100, default='null_name')
    description = models.CharField(max_length=100, default='null_description')
    image = models.ImageField(upload_to='notinator/quiz_images/', default='notinator/quiz_images/default.png')

    questions = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    misc_text = models.CharField(max_length=200, default='null_text')

    class Index:
        indexes = [
            models.Index(fields=['subject' + 'on_subject_index'], name='quiz_subject_index'),
        ]

    def __str__(self):
        return self.name

    def make_quiz(self, input_form: InputForm):
        pass


class Resource(models.Model):
    name = models.CharField(max_length=20, default='null_name')
    description = models.CharField(max_length=200, default='null_description')
    r_link = models.URLField(max_length=200, default='null_link')


class ResourceList(models.Model):
    """
    fields: resouces_name, resources_description, resources_image,
        resource_subject, resources_misc_text, resources, on_subject_index
    methods: make_resources
    """
    subject = models.CharField(max_length=100, default='null_subject')
    on_subject_index = models.IntegerField(default=0)

    name = models.CharField(max_length=100, default='null_name')
    description = models.CharField(max_length=100, default='null_description')
    image = models.ImageField(upload_to='notinator/resources_images/', default='notinator/resources_images/default.png')

    resources = models.ForeignKey(Resource, on_delete=models.CASCADE)
    misc_text = models.CharField(max_length=5000, default='null_text')

    class Index:
        indexes = [
            models.Index(fields=['subject' + 'on_subject_index'], name='resources_subject_index')
        ]

    def __str__(self):
        return self.name

    def make_resources(self, input_form: InputForm):
        pass
