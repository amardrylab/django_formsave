from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import Fullset

# Create your views here.


class QuestionView(CreateView):
	form_class=Fullset
	template_name='question.html'
	success_url='/success/'

	def form_valid(self, form):
		
		self.object= form.save(commit=False)
		self.object.submitby = self.request.path
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

def collectanswer(request, uid, token):
	if request.method=="POST":
		form=Fullset(request.POST)
		if form.is_valid():
			answer=form.save(commit=False)
			answer.submitby=uid+token
			answer.save()
			return HttpResponseRedirect('/success/')
	else:
		form=Fullset()
	return render(request, 'question.html', {'form': form}) 
