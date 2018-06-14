from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
# Create your views here.


class Index(ListView):
    template_name = 'polls\index.html'
    context_object_name = 'latest_question_list' 

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = 'polls\index.html'
#     context = {
#         'latest_question_list':latest_question_list,
#     }
#     return render(request, template, context)


class Detail(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choice'] = Choice.objects.all()
        return context 

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     template = 'polls/detail.html'
#     context = {'question':question}
#     return render(request, template, context) 

class Results(DetailView):
    model = Question
    template_name = 'polls/result.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choice'] = Choice.objects.all()
        return context 


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     template = 'polls/result.html'
#     context = {'question':question}
#     return render(request, template, context)


class CreateQuestion(CreateView):
    model = Question
    fields = ['question_text']

    
    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super().form_valid(form)


class DeleteQuestion(DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')

# class CreateChoice(CreateView):
    
#     def get_object(self):



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

