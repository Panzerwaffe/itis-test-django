from django.forms import ModelForm, TextInput, Form, FloatField
from django.utils.translation import ugettext_lazy as _
from .models import Product


class ProductAddForm(ModelForm):
	class Meta:
		model = Product
		# fields = ['age',
		#           'name',
		#           'weight',
		#           'height']
		# labels = {'age': _("Возраст"),
		#           'name': _("Имя"),
		#           'weight': _("Вес"),
		#           'height': _("Рост")}
		# required = ['__all__']
		# widgets = {
		# 	'weight': TextInput(attrs={'placeholder': '30-150кг'}),
		# }
		# help_texts = {
		# 	'height': _('Ваш рост от 60 до 220 см'),
		# }
