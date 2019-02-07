from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
from .forms import CommentForm


class BlogListView(generic.ListView):
    model = Blog


class BlogDetailsView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailsView, self).get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)