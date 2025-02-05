from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authentication.urls')),
    path('auth/', include('Authentication.urls')),
    path('adm/', include('adm.urls')),
    path('user/', include('user.urls')),
]