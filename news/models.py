#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from django.db import models

from PIL import Image

from datetime import datetime
from django.template.defaultfilters import slugify

def get_image_path(instance, filename):
    return os.path.join('news', 'blink', filename)

class NewsPost(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, editable=False)
	pub_date = models.DateField()
	blurb = models.TextField()
	link = models.URLField(max_length=200)
	modified = models.DateTimeField(auto_now=True)

	image = models.ImageField(upload_to=get_image_path)

	def save(self):
		#self.slug = slugify(self.title)
		#self.modified = datetime.now
		if not self.image:
			return

		super(NewsPost, self).save()
		image = Image.open(self.image)
		(width, height) = image.size
		size = (620, 400)
		image = image.resize(size, Image.ANTIALIAS)
		image.save(self.image.path)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('-pub_date',)
		verbose_name = 'News Post'
		verbose_name_plural = 'News Posts'