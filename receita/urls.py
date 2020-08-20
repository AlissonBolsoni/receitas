from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('site_receita.urls')),
    path('admin/', admin.site.urls),
]