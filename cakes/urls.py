"""
URL configuration for cakes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('admin_home/', views.admin_home),
    path('add_user/', views.add_user),
    path('signup/', views.signup),
    path('login/', views.login ),
    path('user_home/', views.user_home),
    path('cakes/', views.cakes),
    path('add_cakes/', views.add_cakes),
    path('view_users/', views.view_users),
    path('del_user/<int:id>', views.del_user),
    path('user_profile/', views.user_profile),
    path('update_cakes/<int:id>', views.update_cakes),
    path('update_cakes2/<int:id>', views.update_cakes2),
    path('view_cakes/', views.view_cakes),
    path('chocolate_cakes/', views.chocolate_cakes)

    # path('add_cakes1/', views.cakes)
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)