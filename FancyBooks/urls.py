from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('products/', include('products.urls')),
    path('billings/', include('billings.urls')),
    path('admin/', admin.site.urls),
]
