from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^registr/', include('registr.urls')),
        url(r'^', include('start.urls')),
        url(r'^i18n/', include('django.conf.urls.i18n')),
        url(r'^rosetta/', include('rosetta.urls')),
]
