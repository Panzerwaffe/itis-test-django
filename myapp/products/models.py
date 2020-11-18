from django.db import models

class Product(models.Model):
	# user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, default='No title', null=False)
	description = models.CharField(max_length=1000)
	# date =
	price = models.IntegerField()

	class Meta:
		verbose_name = 'product'
		verbose_name_plural = 'products'
		db_table = 'products'

	def __str__(self):
		return f"{self.title}, {self.price}"



