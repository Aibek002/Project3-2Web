from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    cont = models.TextField(blank=True,default='')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Usr', on_delete=models.CASCADE)
    # media = models.ImageField(null=True, blank=True,default='')
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-time_create', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name
