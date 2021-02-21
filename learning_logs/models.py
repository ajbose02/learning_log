from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A model is just a class; it has attributes and methods.


# Here's the model for the topics users will store:
class Topic(models.Model):
    #global variables/attributes
    """A topic the user is learning about"""
    text = models.CharField(max_length=200) #CharField used to store a small amount of text
    data_added = models.DateTimeField(auto_now_add=True) #auto_now_add automatically sets current date/time whenever a Topic is created
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    #toString method, returns the text variable of the user's input
    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    """
    topic is a ForeignKey instance.
    A foreign key is a database term; it's a reference to another record in the database.
    This is the code that connects each entry to a specific topic.
    Each topic is assigned a key, or ID, when created.
    When Django needs to establish a connection between two pieces of data, it uses the key associated with each piece of information.
    We'll use these connections to retrieve all the entries associated with one topic.
    on_delete = models.CASCADE argument tells Django that when a topic is deleted, all of the entries associated with that topic should be deleted as well.
    """
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        #this attribute tells Django to use 'Entries' when it needs to refer to more than 1 Entry
        #Without this, Django would refer to multiple entries as Entrys

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."
