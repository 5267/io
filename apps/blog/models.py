#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField

class Category(models.Model):
	def __unicode__(self):	
		return self.name

	def GetArticleNum(self):
		return Article.objects.filter(category=self).filter(is_publish=True).count()

	def GetAbsoluteURL(self):
		return reverse('category', kwargs={'slug':self.slug})

	name = models.CharField(max_length=64, unique=True)
	slug = models.SlugField(max_length=128, unique=True)

class Tag(models.Model):
	def __unicode__(self):
		return self.name

	def GetArticleNum(self):
		return Article.objects.filter(tag=self).count()

	def GetAbsoluteURL(self):
		return reverse('tag', kwargs={'slug':self.slug})

	name = models.CharField(max_length=64, unique=True)
	slug = models.SlugField(max_length=128, unique=True)

class Article(models.Model):
	def __unicode__(self):
		return self.title

	def GetTags(self):
		return Article.objects.get(id=self.id).tag.all()

	def GetCategory(self):
		return Article.objects.get(id=self.id).category

	def GetAbsoluteURL(self):
		return reverse('article', kwargs={'slug':self.slug})

	title = models.CharField(max_length=128)
	author = models.CharField(max_length=64, default='Anon')
	create_date = models.DateTimeField(default=datetime.now)
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag)
	text = MarkdownField(blank=True, null=True)
	is_publish = models.BooleanField(default=False)
	slug = models.SlugField(max_length=128, unique=True)
