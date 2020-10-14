from django.shortcuts import render

funnyDB = {}

# Create your views here.
def reguser(request):
	global funnyDB
	context = {'funnyDB': funnyDB}

	if request.method == 'POST':
		name = request.POST.get('name', None)
		age = int(request.POST.get('age', None))
		height = float(request.POST.get('height', None))
		context['name'] = name
		context['age'] = age
		context['height'] = height
		context['myrange'] = range(age)

		funnyDB[name] = {'age': age, 'height': height}

		context['funnyDB'] = funnyDB


	return render(request, 'showme.html', context=context)


# Create your views here.
def getuser(request):
	global funnyDB

	context = {'funnyDB': funnyDB}
	if request.method == 'POST':
		name = request.POST.get('name', None)
		context['name'] = name
		context['funnyDB'] = funnyDB

	return render(request, 'showme.html', context=context)

def index(request):
	return render(request, 'index.html')