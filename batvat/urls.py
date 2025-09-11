"""
URL configuration for batvat project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('bats/', views.bat_index, name='bat-index'),
    path('bats/<int:bat_id>/', views.bat_detail, name='bat-detail'),
    path('bats/create/', views.BatCreate.as_view(), name='bat-create'),
    path('bats/<int:pk>/update/', views.BatUpdate.as_view(), name='bat-update'),
    path('bats/<int:pk>/delete/', views.BatDelete.as_view(), name='bat-delete'),
    path(
        'bats/<int:bat_id>/add-feeding/', 
        views.add_feeding, 
        name='add-feeding'
    ),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # Toy URLs
    path('toys/', views.toy_index, name='toy-index'),
    path('toys/<int:toy_id>/', views.toy_detail, name='toy-detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
