"""django_1_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from demo_01 import views
from demo_01.views import index, voice, gesture

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index.as_view()),
    path('gesture/',gesture.as_view()),
    path('voice/',voice.as_view()),
    path('video/',views.get_user_profiles)
]
