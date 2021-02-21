from django.contrib import admin

# Register your models here.

# Importing the model you want to register:
from learning_logs.models import Topic,Entry

# Telling Django to manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)
