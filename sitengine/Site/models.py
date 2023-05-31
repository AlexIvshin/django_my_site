from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Script(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    description = models.CharField(max_length=150, blank=True, db_index=True)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='scripts')

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('script_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=60, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    description = models.CharField(max_length=100, blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='links')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Man(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='mans')

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('man_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Command(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    body = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='commands')

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('command_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Archivefile(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    description = models.CharField(max_length=150, blank=True, db_index=True)
    archivefile = models.FileField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='archivefiles')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
