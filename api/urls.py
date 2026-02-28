from django.urls import path
from .views import (
    ContactView,
    PricingDetailView,
    PricingView,
    ProfileView,
    ProjectDetailView,
    ProjectView,
    ProjectViewHome,
    RegisterView,
)
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
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
    path('pricing/<int:pk>/', PricingDetailView.as_view()),
]
