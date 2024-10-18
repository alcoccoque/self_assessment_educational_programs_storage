from django.urls import include, path
from rest_framework import routers

from self_assessment_educational_programs_storage.users.api.views import (
    StudentViewSet,
    TeacherViewSet,
)
from self_assessment_educational_programs_storage.users.views import (
    teacher_upload,
    user_detail_view,
    user_redirect_view,
    user_update_view,
    teacher_edit,
    teacher_detail,
)

router = routers.SimpleRouter()
router.register(r"student", StudentViewSet, "student")
router.register(r"teacher", TeacherViewSet, "teacher")

app_name = "users"
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("teacher/upload/", teacher_upload, name="teacher_upload"),
    path('teacher/<int:pk>/', teacher_detail, name='teacher_detail'),
    path('teacher/<int:pk>/edit/', teacher_edit, name='teacher_edit'),
]
