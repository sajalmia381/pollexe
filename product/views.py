from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Product, slug=slug)
        return obj
