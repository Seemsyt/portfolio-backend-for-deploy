from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Contact, Pricing, Project
from .paginations import ProjectPagination
from .permissions import IsAdminOrDashboardSecret
from .serializer import (
    ContactSeializer,
    PricingManageSerializer,
    PricingSerializer,
    ProjectSerializer,
    RegisterSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
                "message": "This is protected data",
            }
        )


class DashboardAccessView(generics.GenericAPIView):
    permission_classes = [IsAdminOrDashboardSecret]

    def get(self, request):
        user = request.user
        provided_key = request.headers.get("X-Dashboard-Key", "")
        used_secret_key = bool(provided_key and provided_key == settings.DASHBOARD_SECRET_KEY)

        return Response(
            {
                "allowed": True,
                "username": user.username,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
                "used_secret_key": used_secret_key,
            }
        )


class PricingView(generics.ListCreateAPIView):
    queryset = Pricing.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PricingManageSerializer
        return PricingSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrDashboardSecret()]
        return []


class ContactView(generics.CreateAPIView):
    queryset = Contact
    serializer_class = ContactSeializer


class ProjectViewHome(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination


class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrDashboardSecret()]
        return []


class ProjectDetailView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT", "DELETE"]:
            return [IsAdminOrDashboardSecret()]
        return []


class PricingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingManageSerializer

    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT", "DELETE"]:
            return [IsAdminOrDashboardSecret()]
        return []
