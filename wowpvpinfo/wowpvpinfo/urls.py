
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing.urls')),
    path('wotlk/', include('wotlkdr.urls')),
    path('retail/', include('retaildr.urls')),
    path('admin/', admin.site.urls),
]
