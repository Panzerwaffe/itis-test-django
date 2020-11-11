from django.shortcuts import render
from myapp.histories.models import History
from myapp.histories.forms import IMBForm, FilterByWeightForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

formdict = {(0, 18.5): "Ниже нормального веса",
            (18.5, 25): "Нормальный вес",
            (25, 30): "Избыточный вес",
            (30, 35): "Ожирение I степени",
            (35, 40): "Ожирение II степени",
            (40, 999): "Ожирение III степени"}


def calc_imb(request):
	context = {}

	if request.POST:
		form = IMBForm(request.POST)
		if form.is_valid():
			name = form.data.get('name')
			age = int(form.data.get('age'))
			height = float(form.data.get('height')) / 100
			weight = float(form.data.get('weight'))
			imb = weight / height ** 2

			history = History()
			history.age = age
			history.name = name
			history.weight = weight
			history.height = height
			history.imb = imb
			history.save()

			if imb < 18.5:
				kg = (18.5 - imb) * height ** 2
				context['imb_adwise'] = f"Вам бы добрать {kg} кг"
			elif imb > 25:
				kg = (imb - 25) * height ** 2
				context['imb_adwise'] = f"Вам бы скинуть {kg} кг"
			else:
				context['imb_adwise'] = f"Так держать"

			for k, v in formdict.items():
				if k[0] <= imb <= k[1]:
					context['imb_text'] = v
					break
			context['imb'] = imb
		context['form'] = form
		context['form_filter'] = FilterByWeightForm()

		return render(request, 'showme.html', context=context)
	else:
		form = IMBForm()
		context['form'] = form
		context['form_filter'] = FilterByWeightForm()
		context['histories'] = History.objects.all()
		return render(request, 'showme.html', context=context)


class IMBUpdate(UpdateView):
	model = History
	fields = ['age', 'name', 'weight', 'height']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('index')


class IMBDelete(DeleteView):
	model = History
	success_url = reverse_lazy('index')


# def imb_update(request, history_id):
# 	context = {}
# 	if request.POST:
# 		form = IMB_form(request.POST)
#
# 		if form.is_valid():
# 			old = History.objects.get(id=history_id)
# 			weight = float(form.data.get('weight'))
# 			height = float(form.data.get('height'))
# 			old.name = form.data.get('name')
# 			old.weight = weight
# 			old.height = height
# 			old.imb = weight / height ** 2
# 			old.save()
#
# 			context['form'] = IMB_form()
# 			context['form_filter'] = Filter_by_weight_form()
# 			context['histories'] = History.objects.all()
#
# 			return render(request, 'showme.html', context=context)
# 	else:
# 		history = History.objects.get(id=history_id)
# 		form = IMB_form(initial={'name': history.name,
# 		                         'weight': history.weight,
# 		                         'age': history.age,
# 		                         'height': history.height})
# 		print(form)
# 		context['form'] = form
# 		context['history'] = history
#
# 		return render(request, 'update.html', context=context)


def filter_data(request):
	context = {}
	if request.POST:
		form_filter = FilterByWeightForm(request.POST)
		if form_filter.is_valid():
			context['form'] = IMBForm()
			weight_from = float(form_filter.data.get('weight_from'))
			weight_to = float(form_filter.data.get('weight_to'))
			context['form_filter'] = form_filter
			context['histories'] = History.objects.filter(weight__range=[weight_from, weight_to])

		return render(request, 'showme.html', context=context)


def index(request):
	return render(request, 'index.html')

# context = {}
# if request.method == 'POST':
# 	form = IBM_form(request.POST)
# 	if form.is_valid():
# 		name = form.data.get('name')
# 		weight = float(form.data.get('weight'))
# 		height = float(form.data.get('height'))
#
# 		allusers = MyUser.objects.all()
# 		if name not in (user.username for user in allusers):
# 			user = MyUser()
# 			user.username = name
# 			user.save()
# 		else:
# 			user = allusers.get(username=name)
# 			context['showall'] = History.objects.all()
# 			context['filter_by_weight_form'] = Filter_by_weight_form()
# 			context['calc_ibm_form'] = form
# 			context['warn'] = f"User {user.username} is alreade added his IBM"
# 			return render(request, 'showme.html', context=context)
#
# 		h = History()
# 		h.name = user
# 		h.weight = weight
# 		h.height = height
# 		h.imb = 1
# 		h.f1 = 123456
# 		h.save()
#
# 		print(weight, height, name)
# 		# History.objects.filter(name=name)
# 		# History.objects.get(id=int(???))
#
# 		return redirect('index')
# else:
# 	context['showall'] = History.objects.all()
# 	context['filter_by_weight_form'] = Filter_by_weight_form()
# 	context['calc_ibm_form'] = IBM_form()


#
# def filter_weight(request):
# 	context = {}
# 	if request.method == 'POST':
# 		form = Filter_by_weight_form(request.POST)
# 		if form.is_valid():
# 			weight_from = float(form.data.get('weight_from'))
# 			weight_to = float(form.data.get('weight_to'))
#
# 			weight_by_filter = History.objects.all().filter(weight__range=[weight_from, weight_to])
# 			context['weight_by_filter_list'] = weight_by_filter
# 			context['filter_by_weight_form'] = Filter_by_weight_form()
# 			context['calc_ibm_form'] = IMB_form()
# 			return render(request, 'showme.html', context=context)
#
# 	return render(request, 'showme.html', context=context)
#
