from django.db import models


# Create your models here.

class ResourceList(models.Model):
    """
    fields: resouces_name, resources_description, resources_image,
        resource_subject, resources_misc_text, resources, on_subject_index
    methods: make_resources
    """

    subject = models.CharField(max_length=100, default='null_subject')
    on_subject_index = models.IntegerField(default=0)

    name = models.CharField(max_length=100, default='null_name')
    description = models.CharField(max_length=100, default='null_descriptor')
    image = models.ImageField(upload_to='notinator/resources_images/', default='notinator/resources_images/default.png')

    misc_text = models.CharField(max_length=5000, default='null_text')

    class Index:
        indexes = [
            models.Index(fields=['subject' + 'on_subject_index'], name='resources_subject_index')
        ]


class Resource(models.Model):
    name = models.CharField(max_length=20, default='null_name')
    description = models.CharField(max_length=200, default='null_description')
    r_link = models.URLField(max_length=200, default='null_link')
    resource_list = models.ForeignKey(ResourceList, on_delete=models.CASCADE)


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

    misc_text = models.CharField(max_length=200, default='null_text')

    class Index:
        indexes = [
            models.Index(fields=['subject' + 'on_subject_index'], name='quiz_subject_index'),
        ]


class QuizQuestion(models.Model):
    base_question = True
    multiple_choice_question = False

    name = models.CharField(max_length=200, default='null_name')
    body = models.CharField(max_length=200, default='null_body')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def mark(self, answer: str) -> bool:
        return False

    def get_feedback(self, answer: str) -> str:
        return 'null_feedback'


class QQMultipleChoice(QuizQuestion):
    base_question = False
    multiple_choice_question = True

    choices = list[models.CharField(max_length=200)]
    answer = models.CharField(max_length=200)

    def mark(self, answer: str) -> bool:
        return str == self.answer

    def get_feedback(self, answer: str) -> str:
        if self.mark(answer):
            return 'correct'
        else:
            return format('incorrect. Correct Answer: {}', answer)