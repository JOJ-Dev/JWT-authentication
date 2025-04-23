# backend/server/apps/accounts/urls.py file

from django.urls import re_path as url
from django.urls import include

accounts_urlpatterns = [
    url(r'^api/v1/', include('djoser.urls')),
    url(r'^api/v1/', include('djoser.urls.authtoken')),
]