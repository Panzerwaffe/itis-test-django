from django.shortcuts import render
from myapp.forms import *
from django.shortcuts import redirect

formdict = {(14, 18): "Вы в норме, так держать!",
            (0, 14): "Вам бы набрать вес"}

def calc_ibm(request):
	if request.method == 'POST':
		form = IBM_form(request.POST)
		if form.is_valid():
			name = form.data.get('name')
			weight = float(form.data.get('weight'))
			height = float(form.data.get('height'))

			print(weight, height, name)

			return redirect('index')
	else:
		form = IBM_form()

	return render(request, 'showme.html', context={'form': form})


def index(request):
	return render(request, 'index.html')
