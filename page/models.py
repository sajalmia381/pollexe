from django.db import models
from django.utils import timezone
from pollexe.utils import get_file_name_and_ext

import random


def here_image_name_generator(instance, filename):
    name, ext = get_file_name_and_ext(filename)
    randstr = random.randint(7000, 800000)
    final_name = '{name}{ext}'.format(name=randstr, ext=ext)
    return 'hero/{final_name}'.format(final_name=final_name)


class Hero(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to=here_image_name_generator)
    timestimp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title