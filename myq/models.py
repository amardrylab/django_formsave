from django.db import models
from django.urls import reverse


# Create your models here.

class Set(models.Model):
	opts = (('a', 'a'),
		('b', 'b'),
		('c', 'c'),
		('d', 'd'))
	answer0 = models.CharField(max_length=1, choices=opts)
	answer1 = models.CharField(max_length=1, choices=opts)
	answer2 = models.CharField(max_length=1, choices=opts)
	answer3 = models.CharField(max_length=1, choices=opts)
	answer4 = models.CharField(max_length=1, choices=opts)
	answer5 = models.CharField(max_length=1, choices=opts)
	answer6 = models.CharField(max_length=1, choices=opts)
	answer7 = models.CharField(max_length=1, choices=opts)
	answer8 = models.CharField(max_length=1, choices=opts)
	answer9 = models.CharField(max_length=1, choices=opts)
	submitby= models.CharField(max_length=30)

	def get_absolute_url(self):
		return reverse('success')
