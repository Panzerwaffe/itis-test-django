from django import forms


class IBM_form(forms.Form):
	name = forms.CharField(max_length=20, label="Вашe имя", help_text='введите ваше имя русскими буквами')
	height = forms.FloatField(label="Ваш рост")
	weight = forms.FloatField(label="Ваш вес")
