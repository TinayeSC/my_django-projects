from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    """ This class defines the question object, which the superuser can create
        from the admin page. 

        :param str question_text: This simply stores the actual question. 
        :param date pub_date: This stores the date that the question was published 
            on the site. """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self): 
        """ This method returns the question and displays it to the user"""
        return self.question_text
    
class Choice(models.Model):
    """ This class defines the choice object which will correspond to each question
        
        :param str question: This uses the models module to correspond the question 
            to its possible choice
        :param str choice_text: This stores the text of the different choices.
        :param int votes: This variable stores the number of votes on each choice, and 
            defaults to 0 when creating a new choice. """
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self): 
        """This method displays the choices to the user"""
        return self.choice_text

    
    