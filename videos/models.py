# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify

from django.db import models
from django.utils.translation import gettext_lazy as _


class Video(models.Model):
	name = models.CharField(_('Name'), max_length=100)
	slug = models.SlugField(unique=True, editable=False)
	embed_url = models.URLField(_('Embedded URL'), blank=True, max_length=200)
	thumbnail_url = models.URLField(_('Thumbnail URL'), blank=True, max_length=200)
	description = models.TextField(_('Description'), blank=True)

	modified = models.DateTimeField(auto_now=True)
	view_count = models.IntegerField(default=0, editable=False)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name) # set slug to self
		self.modified = datetime.now
		super(Video, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Video'
		verbose_name_plural = 'Videos'
		ordering = ('modified',)