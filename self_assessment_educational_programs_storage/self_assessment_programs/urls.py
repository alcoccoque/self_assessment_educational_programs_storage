from django.urls import include, path
from rest_framework import routers

from self_assessment_educational_programs_storage.self_assessment_programs.views import (
    InformationOnSelfAssessmentOfEducationalProgramViewSet,
)

router = routers.SimpleRouter()
router.register(
    r" information_on_self_assessment_of_educational_program",
    InformationOnSelfAssessmentOfEducationalProgramViewSet,
    "information-on-self-assessment-of-educational-program",
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
