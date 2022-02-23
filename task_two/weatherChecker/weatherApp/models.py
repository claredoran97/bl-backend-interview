from django.db import models

# Create your models here.
class weatherModel(models.Model):
	city = models.CharField(max_length=100, primary_key=True, unique=True)
	temprature = models.DecimalField(decimal_places=2, max_digits=6)
	queryDate = models.DateTimeField(auto_now=True)

	def _str_(self):
		return self.city
