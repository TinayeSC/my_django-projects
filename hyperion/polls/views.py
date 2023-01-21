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
        
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, "polls/poll.html", context)
   
@login_required(login_url= '//127.0.0.1:8000/user_auth/login/')  
def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
    
@login_required(login_url='//127.0.0.1:8000/user_auth/login/')  
def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
    
@login_required(login_url='//127.0.0.1:8000/user_auth/login/')   
def vote(request, question_id):
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

        