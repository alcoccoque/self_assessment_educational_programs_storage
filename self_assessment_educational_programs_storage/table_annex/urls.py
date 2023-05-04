from django.urls import include, path
from rest_framework import routers

from self_assessment_educational_programs_storage.table_annex.views import (
    EducationalProgramComponentsInformationViewSet,
    ProgramLearningOutcomeCorrespondenceMatrixViewSet,
    TablesAnnexViewSet,
    TeacherSummaryInformationViewSet,
)

router = routers.SimpleRouter()
router.register(
    r"educational_program_components_information",
    EducationalProgramComponentsInformationViewSet,
    "educational-program-components-information",
)
router.register(
    r"program_learning_outcome_correspondence",
    ProgramLearningOutcomeCorrespondenceMatrixViewSet,
    "program-learning-outcome-correspondence",
)
router.register(r"tables_annex", TablesAnnexViewSet, "tables-annex")
router.register(
    r"teacher_summary_information",
    TeacherSummaryInformationViewSet,
    "teacher-summary-information",
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
