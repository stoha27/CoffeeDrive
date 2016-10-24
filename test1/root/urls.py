from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^registr/', include('registr.urls')),
        url(r'^rosetta/', include('rosetta.urls')),
]