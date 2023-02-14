from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login
from django.apps import apps


from user_auth import views 

# Create your views here.





@login_required(login_url = '//127.0.0.1:8000/user_auth/login/')
def index(request):
    """This function will display the different polls to the user, after they have logged in.
    
    :param latest_question_list: This orders, in a list, the polls by the date that they were published
    :type latest_question_list: list
    :param context: This creates a dictionary, with the corresponding text and poll.
    :type context: dictionary""" 
        
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, "polls/poll.html", context)
   
@login_required(login_url= '//127.0.0.1:8000/user_auth/login/')  
def detail(request, question_id):
    """This function will display a specific poll to the user, after they have logged in.
    
        :param question: This is a variable storing the question which the user selected. 
        :type question: str
        """ 
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
    
@login_required(login_url='//127.0.0.1:8000/user_auth/login/')  
def results(request, question_id):
        """This function will display the selected poll to the user and the results after they have
        voted on the poll, after they have logged in.
    
        :param question: This is a variable storing the question which the user selected. 
        :type question: str
        """ 
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
    
@login_required(login_url='//127.0.0.1:8000/user_auth/login/')   
def vote(request, question_id):
        """This function will allow the user to vote on a specific poll, after they have logged in.
            This function also stores the result of the user's vote to display later.
    
            :param question: This is a variable storing the question which the user selected. 
            :type question: str
            :param selected_choice: This variable stores the users choice on the vote. 
                If the user did not select a choice then an error message will appear, and 
                they will be prompted to vote again.
            :param int selected_choice.votes: This is a tally variable. It stores the number of votes
                that are on each choice of a poll question. After a tally has been added to this variable
                the state is stored. 

        """ 
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(
                pk=request.POST['choice']
            )
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice."
    }) 
        else:
            selected_choice.votes += 1
            selected_choice.save()
          # Always return an HttpResponseRedirect after successfully
          # dealing with POST data. This prevents data from being
          # posted twice if a
          # user hits the Back button.
            return HttpResponseRedirect(
                reverse('polls:results', args=(question_id,))
                )

        