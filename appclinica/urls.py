"""appclinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from login.views import *
from appatencion.views import menuView
from django.conf import settings

app_name = 'base'

urlpatterns = [
    path('admin/', admin.site.urls),    
    #path('appatencion/', include('appatencion.urls')),
    path('', IndexView.as_view(), name='index'),  

    path('menu/', login_required(menuView.as_view()), name='menu'),    
    path('empleados_view/', login_required(EmpleadosView.as_view()), name='empleado_view'), 
    #--------------------------------------- login      
    #path('login/', include('login.urls')),
    path('doctor/', CrearDoctorView.as_view(), name='doctor'), 
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('editar_doctor/<int:pk>/',
         EditarDoctorView.as_view(), name='editar_doctor'),
    path('eliminar_paciente/<int:pk>/',
         EliminarDoctorView.as_view(), name='eliminar_doctor'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)










