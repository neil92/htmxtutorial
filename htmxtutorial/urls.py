"""
URL configuration for htmxtutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
from . import views_final

urlpatterns = [
    path('admin/', admin.site.urls),
    # Basic HTMX Tutorial
    path("", views.index, name="index"),
    path("snippet", views.snippet, name="snippet"),
    # Search Contacts Table Tutorial
    path("contacts", views.contacts, name="contacts"),
    path("contacts_final", views_final.contacts_final, name="contacts_final"),
    path("search_final", views_final.search_final, name="search_final"),
]
