from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save


class SocialLink(models.Model):
    name = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    icon = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(SocialLink, self).save(*args, **kwargs)


# def social_link_save_action(instance, sender, created, *args, **kwargs):
#     if created:
#         print(instance)
#
#
# post_save.connect(social_link_save_action, sender=SocialLink)


class AppOption(models.Model):
    logo = models.ImageField()
    logo_2 = models.ImageField(blank=True, null=True)

    bio = models.TextField(blank=True, null=True)

    # social = models.ManyToManyField(SocialLink, blank=True)

    def __str__(self):
        return self.__class__.__name__

    def save(self, *args, **kwargs):

        if self.pk is not 1:
            self.pk = 1

        """
        # ================== One + instance create validation Error Throw
        if AppOption.objects.exists() and not self.pk:
            raise ValidationError("Can' Allow Another Instance For App Option")
        """
        return super(AppOption, self).save(*args, **kwargs)