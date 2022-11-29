from django.urls import path
from rest_framework import viewsets, routers
from .views import AllPost_ViewSet,OnePost_ViewSet,Comment_ViewSet

router = routers.DefaultRouter()

router.register(r'comment', Comment_ViewSet, basename='comment')

urlpatterns = [
  path('posts', AllPost_ViewSet.as_view()),
  path('posts/<int:id>', OnePost_ViewSet.as_view()),
  path('posts/<int:id>/comments', Comment_ViewSet.as_view()),
]