"""testTwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from tweets.views import UserProfile_ViewSet, Post_ViewSet, All_Comment_ViewSet

router = routers.DefaultRouter()

router.register(r'profiles', UserProfile_ViewSet, basename='profiles')
router.register(r'posts', Post_ViewSet, basename='posts')
router.register(r'comments', All_Comment_ViewSet, basename='comments')
# router.register(r'comments', Comment_ViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('tweets.urls')),
    path('', include('user_auth.urls')),
    # path('comments', Comment_ViewSet.as_view()),


    path('admin/', admin.site.urls),
]
