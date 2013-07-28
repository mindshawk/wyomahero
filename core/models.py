# -*- coding: utf-8 -*-
from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	email = models.EmailField(max_length=200)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now=True, editable=False)

	def __unicode__(self):
		return self.first_name, self.last_name

	class Meta:
		ordering = ('-timestamp',)
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def get_absolute_url(self):
		return reverse('contact_detail', kwargs={'email': self.email})
