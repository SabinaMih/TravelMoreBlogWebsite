from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include   # include --> updating file to point at our pages app and then within pages we match the views to routes



urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls), 
    path('blogs/', include('blogs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),      # path which defines the account/url where we will place our log in and log out pages
    path('accounts/', include('accounts.urls')),                 # by creating this line of code we are pointing to new app directly below where we include the built-in auth app  
    path('', include('pages.urls')),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
