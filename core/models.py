from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	email = models.EmailField(max_length=200)
	message = models.TextField()
