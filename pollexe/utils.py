from django.utils.text import slugify
import os
import string
import random


def get_random_string_generator(size=10, char=string.ascii_lowercase):
    return ''.join(random.choice(char) for _ in random(size))


def get_file_name_and_ext(basename):
    base_file = os.path.basename(basename)
    name, ext = os.path.splitext(base_file)
    return name, ext


def get_unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        try:
            slug = slugify(instance.title)
        except AttributeError:
            slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = '{slug}-{random_str}'.format(slug=slug, random_str=get_random_string_generator())
        return new_slug
    return slug


# ===================================== User image Name Save
def get_user_image_name(instance, basename):
    name, ext = get_file_name_and_ext(basename)
    randstr = random.randint(7000, 800000)
    final_name = '{name}{ext}'.format(name=randstr, ext=ext)
    return 'user/{final_name}'.format(final_name=final_name)


def get_image_dir_and_name(instance, basename):
    name, ext = get_file_name_and_ext(basename)
    randstr = random.randint(7000, 800000)
    final_name = '{name}{ext}'.format(name=randstr, ext=ext)
    return '{klass}/{final_name}'.format(klass=instance.__class__.__name__.lower(), final_name=final_name)
