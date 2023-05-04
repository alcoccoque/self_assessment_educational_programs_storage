from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from self_assessment_educational_programs_storage.users.api.serializers import (
    StudentSerializer,
    TeacherSerializer,
    UserSerializer,
)
from self_assessment_educational_programs_storage.users.models import Student, Teacher

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
