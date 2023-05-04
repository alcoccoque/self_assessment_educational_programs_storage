from django.urls import include, path
from rest_framework import routers

from self_assessment_educational_programs_storage.general_information.views import (
    EducationProgramAccreditationInformationViewSet,
    EducationProgramDocumentViewSet,
    EducationProgramGeneralInformationViewSet,
    EducationProgramViewSet,
    EducationStatisticsViewSet,
    FieldOfStudyViewSet,
    GeneralInformationViewSet,
    HEILinksInEDEBOViewSet,
    HigherEducationInstitutionAreaViewSet,
    HigherEducationInstitutionInformationViewSet,
    HigherEducationInstitutionViewSet,
    OtherHigherEducationProgramViewSet,
    SelfAssessmentEducationalProgramRestrictedInfoViewSet,
    SeparateStructuralUnitViewSet,
    SpecialtyViewSet,
    StructuralSubdivisionViewSet,
)

router = routers.SimpleRouter()
router.register(
    r"education_program",
    EducationProgramViewSet,
    "education-program",
)
router.register(
    r"education_program_accreditation_information",
    EducationProgramAccreditationInformationViewSet,
    "education-program-accreditation-information",
)
router.register(
    r"education_program_document",
    EducationProgramDocumentViewSet,
    "education-program-document",
)
router.register(
    r"education_program_general_information",
    EducationProgramGeneralInformationViewSet,
    "education-program-general-information",
)
router.register(
    r"education_statistics",
    EducationStatisticsViewSet,
    "education-statistics",
)
router.register(
    r"field_of_study",
    FieldOfStudyViewSet,
    "field-of-study",
)
router.register(
    r"general_information",
    GeneralInformationViewSet,
    "general-information",
)
router.register(
    r"hei_links_in_edebo",
    HEILinksInEDEBOViewSet,
    "hei-links-in-edebo",
)
router.register(
    r"higher_education_institution",
    HigherEducationInstitutionViewSet,
    "higher-education-institution",
)
router.register(
    r"higher_education_institution_area",
    HigherEducationInstitutionAreaViewSet,
    "higher-education-institution-area",
)
router.register(
    r"higher_education_institution_information",
    HigherEducationInstitutionInformationViewSet,
    "higher-education-institution-information",
)
router.register(
    r"other_higher_education_program",
    OtherHigherEducationProgramViewSet,
    "other-higher-education-program",
)
router.register(
    r"self_assessment_educational_program_restricted_info",
    SelfAssessmentEducationalProgramRestrictedInfoViewSet,
    "self-assessment-educational-program-restricted-info",
)
router.register(
    r"separate_structural_unit",
    SeparateStructuralUnitViewSet,
    "separate-structural-unit",
)
router.register(
    r"specialty",
    SpecialtyViewSet,
    "specialty",
)
router.register(
    r"structural_subdivision",
    StructuralSubdivisionViewSet,
    "structural-subdivision",
)


urlpatterns = [
    path("api/v1/", include(router.urls)),
]
