from django.contrib import admin

#usando assim, podemos chamar as urls de cada app
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastros.urls')),
]
