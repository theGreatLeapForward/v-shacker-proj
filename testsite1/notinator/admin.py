from django.contrib import admin

from .models import Quiz, Resources

# admins can manually make custom quizzes/resources
admin.site.register(Quiz)
admin.site.register(Resources)

# Register your models here.
