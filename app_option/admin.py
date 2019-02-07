from django.contrib import admin
from .models import *


class SocialLinkAdmin(admin.ModelAdmin):

    class Meta:
        model = SocialLink


admin.site.register(SocialLink, SocialLinkAdmin)


# class AppOptionInline(admin.TabularInline):
#     model = AppOption.social.through
#     extra = 1


class AppOptionAdmin(admin.ModelAdmin):

    # inlines = [AppOptionInline]
    # exclude = ['social', ]

    def has_add_permission(self, request, obj=None):
        return AppOption.objects.all().count() < 1

    def has_delete_permission(self, request, obj=None):
        return AppOption.objects.all().count() != 1

    class Meta:
        model = AppOption


admin.site.register(AppOption, AppOptionAdmin)
