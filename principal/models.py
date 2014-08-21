from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):

	user = models.ForeignKey(User)
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=200)

	def __unicode__(self):
		return self.title