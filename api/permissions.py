from django.conf import settings
from rest_framework.permissions import BasePermission


class IsAdminOrDashboardSecret(BasePermission):
    """Allow only authenticated admin users or requests with the dashboard secret key."""

    message = "Dashboard access denied. Admin privileges or valid secret key required."

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_staff or user.is_superuser:
            return True

        secret_key = request.headers.get("X-Dashboard-Key", "")
        return bool(secret_key) and secret_key == settings.DASHBOARD_SECRET_KEY
