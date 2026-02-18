from django.urls import path
from .views import ProfileView, RegisterView,PricingView,ContactView,ProjectViewHome,ProjectView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path('pricing/',PricingView.as_view()),
    path('contact/',ContactView.as_view()),
    path('projects/home/',ProjectViewHome.as_view()),
    path('projects/',ProjectView.as_view()),
]
