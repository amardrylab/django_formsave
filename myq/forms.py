from django import forms
from .models import Set

class Fullset(forms.ModelForm):
	opts = (('a', 'a'),
		('b', 'b'),
		('c', 'c'),
		('d', 'd'))
	answer0=forms.CharField(widget=forms.Select(choices=opts))
	answer1=forms.CharField(widget=forms.Select(choices=opts))
	answer2=forms.CharField(widget=forms.Select(choices=opts))
	answer3=forms.CharField(widget=forms.Select(choices=opts))
	answer4=forms.CharField(widget=forms.Select(choices=opts))
	answer5=forms.CharField(widget=forms.Select(choices=opts))
	answer6=forms.CharField(widget=forms.Select(choices=opts))
	answer7=forms.CharField(widget=forms.Select(choices=opts))
	answer8=forms.CharField(widget=forms.Select(choices=opts))
	answer9=forms.CharField(widget=forms.Select(choices=opts))

	class Meta:
		model=Set
		exclude=['submitby']
