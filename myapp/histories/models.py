from django.db import models


class History(models.Model):
	# name = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	age = models.IntegerField()
	name = models.CharField(max_length=100)
	weight = models.FloatField()
	height = models.FloatField()
	imb = models.FloatField()

	class Meta:
		verbose_name = 'history'
		verbose_name_plural = 'histories'
		db_table = 'histories'

	def __str__(self):
		return f"{self.name}, {self.weight}"



