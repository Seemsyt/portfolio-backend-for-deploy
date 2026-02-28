from django.shortcuts import render
from rest_framework import generics

from api.models import Contact, Pricing, Project
from .serializer import (
    ContactSeializer,
    PricingManageSerializer,
    PricingSerializer,
    ProjectSerializer,
    RegisterSerializer,
)
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import RegisterSerializer
from .paginations import ProjectPagination

# Register
class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# Protected Profile View
class ProfileView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "message": "This is protected data"
        })
class PricingView(generics.ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
class ContactView(generics.CreateAPIView):
    queryset = Contact
    serializer_class = ContactSeializer

class ProjectViewHome(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination

class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PricingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingManageSerializer
