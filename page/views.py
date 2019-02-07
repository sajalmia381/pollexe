from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import SingleObjectMixin
from .models import Hero
from blog.models import Blog


class IndexView(generic.ListView):
    template_name = 'page/index.html'
    model = Hero

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['latest_themes'] = Blog.objects.all()[:4]
        return context


