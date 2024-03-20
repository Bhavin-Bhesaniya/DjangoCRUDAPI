from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CrudApp.urls')),
    path('api/v1/', include('api.urls')),
]
