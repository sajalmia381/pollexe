from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('account.urls', namespace='account')),
    path('', include('page.urls', namespace='page')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('product.urls', namespace='product')),

    # admin
    path('admin/', admin.site.urls),
    # Third party
    path('summernote/', include('django_summernote.urls')),
    path('front-edit/', include('front.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
