from django.urls import include, path
from rest_framework import routers

from self_assessment_educational_programs_storage.general_question_answer.views import (
    ControlMeasuresAndAcademicIntegrityViewSet,
    EducationalEnvironmentAndMaterialResourcesViewSet,
    EducationalProgramAccessViewSet,
    EducationalProgramDesignViewSet,
    EducationalProgramDevelopmentPerspectivesViewSet,
    EducationalProgramLearningAndTeachingViewSet,
    EducationalProgramStructureAndContentViewSet,
    EducationalProgramViewSet,
    EducationalTransparencyAndPublicityViewSet,
    GeneralQuestionAnswerViewSet,
    HumanResourcesViewSet,
    LanguageViewSet,
    QualityAssuranceViewSet,
)
from self_assessment_educational_programs_storage.table_annex.views import (
    EducationalProgramComponentsInformationViewSet,
    ProgramLearningOutcomeCorrespondenceMatrixViewSet,
    TablesAnnexViewSet,
    TeacherSummaryInformationViewSet,
)

router = routers.SimpleRouter()
router.register(
    r"control_measures_and_academic_integrity",
    ControlMeasuresAndAcademicIntegrityViewSet,
    "control-measures-and-academic-integrity",
)
router.register(
    r"educational_environment_and_material_resources",
    EducationalEnvironmentAndMaterialResourcesViewSet,
    "educational-environment-and-material-resources",
)
router.register(
    r"educational_program",
    EducationalProgramViewSet,
    "educational-program",
)
router.register(
    r"educational_program_access",
    EducationalProgramAccessViewSet,
    "educational-program-access",
)
router.register(
    r"educational_program_design",
    EducationalProgramDesignViewSet,
    "educational-program-design",
)
router.register(
    r"educational_program_development_perspectives",
    EducationalProgramDevelopmentPerspectivesViewSet,
    "educational-program-development-perspectives",
)
router.register(
    r"educational_program_learning_and_teaching",
    EducationalProgramLearningAndTeachingViewSet,
    "educational-program-learning-and-teaching",
)
router.register(
    r"educational_program_structure_and_content",
    EducationalProgramStructureAndContentViewSet,
    "educational-program-structure-and-content",
)
router.register(
    r"educational_transparency_and_publicity",
    EducationalTransparencyAndPublicityViewSet,
    "educational-transparency-and-publicity",
)
router.register(
    r"general_question_answer",
    GeneralQuestionAnswerViewSet,
    "general-question-answer",
)
router.register(
    r"human_resources",
    HumanResourcesViewSet,
    "human_resources",
)
router.register(
    r"language",
    LanguageViewSet,
    "language",
)
router.register(
    r"quality_assurance",
    QualityAssuranceViewSet,
    "quality-assurance",
)


urlpatterns = [
    path("api/v1/", include(router.urls)),
]
