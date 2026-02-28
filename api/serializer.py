from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Contact, Pricing, Project

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }
    def validate_email(self,value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError('email already exists')
        return value
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
class PricingSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    class Meta:
        model = Pricing
        fields = ['id', 'title', 'price', 'features', 'slug', 'is_admin']

    def get_features(self, obj):
        return list(filter(None, [
            obj.feature_1,
            obj.feature_2,
            obj.feature_3,
            obj.feature_4,
            obj.feature_5,
            obj.feature_6,
        ]))

class PricingManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = [
            'id',
            'title',
            'price',
            'slug',
            'is_admin',
            'feature_1',
            'feature_2',
            'feature_3',
            'feature_4',
            'feature_5',
            'feature_6',
        ]
class ContactSeializer(serializers.ModelSerializer):
    class Meta :
        model = Contact
        fields = ['name','email','message']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
