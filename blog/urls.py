from django.urls import path

from .views import *
app_name = 'blog'
urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug>', BlogDetailsView.as_view(), name='blog_details'),
]