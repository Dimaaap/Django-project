from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index_page.urls')),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('search/', include('search.urls')),
    path('send/', include('send_emails.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
