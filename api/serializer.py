from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Contact, Pricing, Project


class RegisterSerializer(serializers.ModelSerializer):
    is_superuser = serializers.BooleanField(write_only=True, required=False, default=False)
    admin_secret_key = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "is_superuser", "admin_secret_key"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already exists")
        return value

    def validate(self, attrs):
        wants_superuser = attrs.get("is_superuser", False)
        supplied_secret = attrs.get("admin_secret_key", "")

        if wants_superuser and supplied_secret != settings.DASHBOARD_SECRET_KEY:
            raise serializers.ValidationError(
                {"admin_secret_key": ["Valid admin secret key is required for superuser creation."]}
            )

        return attrs

    def create(self, validated_data):
        wants_superuser = validated_data.pop("is_superuser", False)
        validated_data.pop("admin_secret_key", None)

        if wants_superuser:
            user = User.objects.create_superuser(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )
        else:
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )
        return user


class PricingSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()

    class Meta:
        model = Pricing
        fields = ["id", "title", "price", "features", "slug", "is_admin"]

    def get_features(self, obj):
        return list(
            filter(
                None,
                [
                    obj.feature_1,
                    obj.feature_2,
                    obj.feature_3,
                    obj.feature_4,
                    obj.feature_5,
                    obj.feature_6,
                ],
            )
        )


class PricingManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = [
            "id",
            "title",
            "price",
            "slug",
            "is_admin",
            "feature_1",
            "feature_2",
            "feature_3",
            "feature_4",
            "feature_5",
            "feature_6",
        ]


class ContactSeializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
