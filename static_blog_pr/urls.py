"""
URL configuration for static_blog_pr project.

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
from django.urls import path,include
from static_blog_app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",show,name="Des-block"),
    path("",login_main,name="login-portal"),
    path("about/",about,name="about"),
    path("content/",content,name="content"),
    path("write/",nothing,name="nothing"),
    path("Aiblog/",ai_blog,name="Ai-blog"),
    path("stockblog/",stock_blog,name="stock-blog"),
    path('cryptoblog/',crypto_blog,name="crypto-blog"),
    path("register/",register,name="register"),
    path('logout/',logout_main,name='logout')
]
