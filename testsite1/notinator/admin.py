from django.contrib import admin

from .models import Quiz, ResourceList

# admins can manually make custom quizzes/resources
admin.site.register(Quiz)
admin.site.register(ResourceList)

# Register your models here.
