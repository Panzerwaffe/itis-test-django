from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import render


class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'


def logout_view(request):
	logout(request)

def account(request):
	context = {'user': request.user.username,
	           'content': 'HELLO'}

	return render(request, 'users/account.html', context=context)
