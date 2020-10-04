 
from django.contrib import admin
from django.urls import path, include

from login.views import LoginView, IndexView
from appatencion.views import menuView, opcionesView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),    
    path('index/', IndexView.as_view(), name='index'),  
    path('menu/', menuView.as_view(), name='menu'),
    path('opciones/', opcionesView.as_view(), name='opciones'),
    path('base/', include('appcore.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
