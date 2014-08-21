from django import forms
from .models import Question

class LoginForm(forms.Form):

	username = forms.CharField(max_length = 50)
	password = forms.CharField(max_length = 50,
			widget = forms.TextInput(attrs = {
					'type' : 'password'
				}))

class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		exclude = ('user',)