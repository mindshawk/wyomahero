#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from django.db import models

from PIL import Image

def get_image_path(instance, filename):
    return os.path.join('people', filename)

class Person(models.Model):
	name = models.CharField(max_length=80)
	title = models.CharField(max_length=80)
	email = models.EmailField(max_length=200)
	linkedin = models.URLField(max_length=200)
	vimeo = models.URLField(max_length=200, blank=True)

	image = models.ImageField(upload_to=get_image_path)

	fun_fact = models.CharField(max_length=200, blank=True)

	bio = models.TextField()

	def save(self):
		if not self.image:
			return

		super(Person, self).save()
		image = Image.open(self.image)
		(width, height) = image.size
		size = (300, 300)
		image = image.resize(size, Image.ANTIALIAS)
		image.save(self.image.path)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'People'