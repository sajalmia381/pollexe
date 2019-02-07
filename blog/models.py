import random
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import pre_save
from django.urls import reverse
from pollexe.utils import *


User = get_user_model()


def get_blog_image_name(instance, basename):
    name, ext = get_file_name_and_ext(basename)
    randstr = random.randint(7000, 800000)
    final_name = '{name}{ext}'.format(name=randstr, ext=ext)
    return 'blog/{final_name}'.format(final_name=final_name)


BLOG_TYPE = (
    ('collection', 'Collection'),
    ('review', 'Review'),
)

STATUS = (
    ('published', 'Published'),
    ('pending', 'Pending'),
)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


def tag_slug_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(tag_slug_pre_save, sender=Tag)


class Blog(models.Model):
    type = models.CharField(max_length=20, choices=BLOG_TYPE, default='collection')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=25, choices=STATUS, default='pending')
    title = models.CharField(max_length=250)
    slug = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        help_text='This slug will used for page URL. For same like Title URL leave blank'
    )
    image = models.ImageField(upload_to=get_image_dir_and_name, blank=True, null=True)
    content = models.TextField(blank=True)

    tag_list = models.ManyToManyField(Tag, blank=True)

    is_public = models.BooleanField(default=True)
    is_feature = models.BooleanField(default=False)

    timestimp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    updatestimp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_details', kwargs={'slug': self.slug})


def blog_slug_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(blog_slug_pre_save, sender=Blog)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField(blank=True)
    content = models.TextField()
    timestimp = models.DateTimeField(auto_now_add=False, auto_now=False, default=timezone.now)

    def __str__(self):
        return 'Comment on: {blog} by {email}'.format(blog=self.blog.pk, email=self.email)