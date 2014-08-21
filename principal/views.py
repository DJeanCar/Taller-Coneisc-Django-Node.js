import json
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import LoginForm, QuestionForm
from .models import Question

class HomeView(FormView):

	template_name = 'home.html'
	form_class = LoginForm
	success_url = '/index/'

	def form_valid(self, form):
		acceso = authenticate(username = form.cleaned_data['username'],
						password = form.cleaned_data['password'])
		if acceso:
			login(self.request, acceso)
		return super(HomeView, self).form_valid(form)

class IndexView(CreateView):

	template_name = 'index.html'
	form_class = QuestionForm
	success_url = '/index/'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['questions'] = Question.objects.all().order_by('-id')
 		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(IndexView, self).form_valid(form)




def LogOut(request):
	logout(request)
	return redirect('/')

@csrf_exempt
def crear(request):
	user = User.objects.get(username = request.POST['username'])
	Question.objects.create(user= user, title= request.POST['title'], content=request.POST['content'])
	response = { 'username' : request.POST['username'],
				'title' : request.POST['title'],
				'content' : request.POST['content'] }
	return HttpResponse(json.dumps(response), content_type = 'application/json')
