from django.contrib import admin

from .models import Quiz, ResourceList, QuizQuestion, Resource, QQMultipleChoice

# admins can manually make custom quizzes/resources
admin.site.register(Quiz)
admin.site.register(ResourceList)
admin.site.register(Resource)
admin.site.register(QuizQuestion)
admin.site.register(QQMultipleChoice)


# Register your models here.
