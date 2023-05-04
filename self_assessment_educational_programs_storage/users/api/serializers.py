from django.contrib.auth import get_user_model
from rest_framework import serializers

from self_assessment_educational_programs_storage.users.models import Student, Teacher

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class StudentSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = Teacher
        fields = "__all__"
