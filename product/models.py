from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils import timezone
from django.urls import reverse

from .utils import get_unique_slug_generator, get_product_images_name

User = get_user_model()


# ====================== Tag
class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name


def tag_slug_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(tag_slug_pre_save, sender=Tag)


# ==================== Product Type
class ProductType(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name


def product_type_slug_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(product_type_slug_pre_save, sender=ProductType)


# ==================== Product Category
class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name


def product_category_slug_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(product_category_slug_pre_save, sender=ProductCategory)


class ProductQuerySet(models.query.QuerySet):

    def is_public(self):
        return self.filter(is_public=True)


class ProductModelManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().is_public()


def get_sentinel_user():
    return User.objects.get_or_create(email='deleted@user.com', is_active=True)[0]


def get_product_type():
    return ProductType.objects.get_or_create(name='other')[1]


# ==================== Product Category
class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), blank=True, null=True)
    category = models.ManyToManyField(ProductCategory)
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    images = models.ImageField(upload_to=get_product_images_name, blank=True)
    content = models.TextField()

    demo_link = models.URLField(blank=True, null=True)
    affiliate_link = models.URLField(blank=True, null=True)
    host_link = models.URLField(blank=True, null=True)

    is_public = models.BooleanField(default=True)
    is_feature = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)

    timestimp = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    updatestimp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = ProductModelManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-timestimp', )


def product_slug_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = get_unique_slug_generator(instance)


pre_save.connect(product_slug_pre_save, sender=Product)