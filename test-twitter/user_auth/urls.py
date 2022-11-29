from django.urls import path
from .views import SignupView,LoginView,GrabProfile, Verify
urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', GrabProfile.as_view()),
    path('verify', Verify.as_view())
]