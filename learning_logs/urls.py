"""Defines URL patterns for learning_logs."""

from django.urls import path
#path function needed when mapping URls to views

from . import views
# . implies that we're importing from the same directory as this urls.py file

app_name = 'learning_logs'
#helps Django distinguish this urls.py file from files of the same name in other apps within the project

urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),

    #Show all topics.
    path('topics/', views.topics, name='topics'),
    #Any request with a URL that matches this pattern will then be passed to the function topics() in views.py

    #detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),

    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    #Deleting a topic
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]

"""path function takes 3 arguments:
1) String that helps Django route the current request properly
2) Specifies which view function to call
3) Provides the name index for this URL pattern so we can refer to it in other sections of the code

"""
