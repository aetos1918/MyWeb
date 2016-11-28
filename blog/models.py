from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models as m
from django.template.defaultfilters import truncatewords
from django.utils import timezone


# Create your models here.


class Post(m.Model):
    Title = m.CharField(max_length=100)
    slug = m.SlugField(max_length=150, unique_for_date='publish')
    Body = m.TextField()
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'))
    status = m.CharField(max_length=10, choices=STATUS_CHOICES,
                         default='Draft')
    created_by = m.ForeignKey(User)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    publish = m.DateTimeField(default=timezone.now())


    class Meta:
        ordering = ('-publish', '-updated')

    def __str__(self):
        return self.Title

    @property
    def short_body(self):
        return truncatewords(self.Body, 30)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])
