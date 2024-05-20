"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from air.views import *
from . import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home ,name="home"),

    path('category<int:id>/',category ,name="category"),

    
    path('batafsil/<int:id>/',batafsil ,name="batafsil"),

    path('create_air/',create_air ,name="create_air"),
    path('update_air/<int:id>/',update_air ,name="update_air"),
    path('delete_air/<int:id>/',delete_air ,name="delete_air"),

    path('reys<int:id>/',reys ,name="reys"),
    path('city<int:id>/',city ,name="city"),

    path('more/<int:id>/',more ,name="more"),

    path('create_city/',create_city ,name="create_city"),
    path('update_city/<int:id>/',update_city ,name="update_city"),
    path('delete_city/<int:id>/',delete_city ,name="delete_city")


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
