from django.contrib import admin
# third party
from django_summernote.admin import SummernoteModelAdmin
from .models import *

admin.site.register(ProductCategory)

admin.site.register(ProductType)


class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    exclude = ('author',)
    summernote_fields = ('content',)

    class Meta:
        model = Product

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)

admin.site.register(Tag)