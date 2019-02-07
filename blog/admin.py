from django.contrib import admin

from .models import *

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Tag)


class BlogInlineAdmin(admin.TabularInline):
    model = Comment
    max_num = 1


class BlogAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ['content', ]
    list_display = ['title', 'pk', 'author', 'is_public', 'is_feature', 'timestimp', 'updatestimp']
    inlines = [BlogInlineAdmin]
    fieldsets = (
        (None, {'fields': ('type', 'title', 'image', 'content', )}),

        ('Tags', {
            'fields': ('tag_list',)
        }),

        ('Post Permissions', {
            'fields': ('status', 'is_public', 'is_feature')
        }),
        ('URLS', {
            'classes': ('collapse', 'open'),
            'fields': ('slug',)
        }),
        ('Publication', {
            'classes': ('collapse', ),
            'fields': ('timestimp', 'updatestimp',)
        }),
        ('Author', {
            'classes': ('collapse', ),
            'fields': ('author',),
        }),
    )

    class Meta:
        model = Blog

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        if request.user.is_admin:
            obj.status = 'Published'
        super().save_model(request, obj, form, change)


admin.site.register(Blog, BlogAdmin)