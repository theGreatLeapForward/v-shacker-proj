from django.db import models

from .forms import InputForm

# Create your models here.


class Quiz(models.Model):
    """
    fields: quiz_name, quiz_description, quiz_image, question_amount
    quiz_questions fields: name, body, answer_type, possible choices

    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='notinator/quiz_images/', default='notinator/quiz_images/default.png')
    quiz_question_amount = models.IntegerField(default=0)

    question_names = list[models.CharField(max_length=20)]
    question_bodies = list[models.CharField(max_length=200)]
    question_answer_types = list[models.IntegerField(max_length=1, default=0)]

    # optional fields
    question_choices = list[list[models.CharField(max_length=20)]]

    def __str__(self):
        return self.name

    def make_quiz(self, input_form: InputForm):
        pass


class Resources(models.Model):
    """
    fields: resouces_name, resources_description, resources_image, resources_amount
    resource_fields: name, link
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='notinator/resources_images/', default='notinator/resources_images/default.png')
    resources_amount = models.IntegerField(default=0)

    resource_names = list[models.CharField(max_length=20)]
    resource_links = list[models.URLField(max_length=200)]

    misc_resources_text = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

    def make_resources(self, input_form: InputForm):
        pass
