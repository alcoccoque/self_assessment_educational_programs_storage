from rest_framework import viewsets

from .models import (
    ControlMeasuresAndAcademicIntegrity,
    EducationalEnvironmentAndMaterialResources,
    EducationalProgram,
    EducationalProgramAccess,
    EducationalProgramComponentsInformation,
    EducationalProgramDesign,
    EducationalProgramDevelopmentPerspectives,
    EducationalProgramLearningAndTeaching,
    EducationalProgramStructureAndContent,
    EducationalTransparencyAndPublicity,
    EducationProgram,
    EducationProgramAccreditationInformation,
    EducationProgramDocument,
    EducationProgramGeneralInformation,
    EducationStatistics,
    Employee,
    FieldOfStudy,
    GeneralInformation,
    GeneralQuestionAnswer,
    HEILinksInEDEBO,
    HigherEducationInstitution,
    HigherEducationInstitutionArea,
    HigherEducationInstitutionInformation,
    HumanResources,
    InformationOnSelfAssessmentOfEducationalProgram,
    Language,
    OtherHigherEducationProgram,
    ProgramLearningOutcomeCorrespondenceMatrix,
    QualityAssurance,
    SelfAssessmentEducationalProgramRestrictedInfo,
    SeparateStructuralUnit,
    Specialty,
    StructuralSubdivision,
    TablesAnnex,
    TeacherSummaryInformation,
)
from .serializers import (
    ControlMeasuresAndAcademicIntegritySerializer,
    EducationalEnvironmentAndMaterialResourcesSerializer,
    EducationalProgramAccessSerializer,
    EducationalProgramComponentsInformationSerializer,
    EducationalProgramDesignSerializer,
    EducationalProgramDevelopmentPerspectivesSerializer,
    EducationalProgramLearningAndTeachingSerializer,
    EducationalProgramSerializer,
    EducationalProgramStructureAndContentSerializer,
    EducationalTransparencyAndPublicitySerializer,
    EducationProgramAccreditationInformationSerializer,
    EducationProgramDocumentSerializer,
    EducationProgramGeneralInformationSerializer,
    EducationProgramSerializer,
    EducationStatisticsSerializer,
    EmployeeSerializer,
    FieldOfStudySerializer,
    GeneralInformationSerializer,
    GeneralQuestionAnswerSerializer,
    HEILinksInEDEBOSerializer,
    HigherEducationInstitutionAreaSerializer,
    HigherEducationInstitutionInformationSerializer,
    HigherEducationInstitutionSerializer,
    HumanResourcesSerializer,
    InformationOnSelfAssessmentOfEducationalProgramSerializer,
    LanguageSerializer,
    OtherHigherEducationProgramSerializer,
    ProgramLearningOutcomeCorrespondenceMatrixSerializer,
    QualityAssuranceSerializer,
    SelfAssessmentEducationalProgramRestrictedInfoSerializer,
    SeparateStructuralUnitSerializer,
    SpecialtySerializer,
    StructuralSubdivisionSerializer,
    TablesAnnexSerializer,
    TeacherSummaryInformationSerializer,
)


class ControlMeasuresAndAcademicIntegrityViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = ControlMeasuresAndAcademicIntegrity.objects.all()
    serializer_class = ControlMeasuresAndAcademicIntegritySerializer


class EducationalEnvironmentAndMaterialResourcesViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalEnvironmentAndMaterialResources.objects.all()
    serializer_class = EducationalEnvironmentAndMaterialResourcesSerializer


class EducationalProgramViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgram.objects.all()
    serializer_class = EducationalProgramSerializer


class EducationalProgramAccessViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramAccess.objects.all()
    serializer_class = EducationalProgramAccessSerializer


class EducationalProgramComponentsInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramComponentsInformation.objects.all()
    serializer_class = EducationalProgramComponentsInformationSerializer


class EducationalProgramDesignViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramDesign.objects.all()
    serializer_class = EducationalProgramDesignSerializer


class EducationalProgramDevelopmentPerspectivesViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramDevelopmentPerspectives.objects.all()
    serializer_class = EducationalProgramDevelopmentPerspectivesSerializer


class EducationalProgramLearningAndTeachingViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramLearningAndTeaching.objects.all()
    serializer_class = EducationalProgramLearningAndTeachingSerializer


class EducationalProgramStructureAndContentViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramStructureAndContent.objects.all()
    serializer_class = EducationalProgramStructureAndContentSerializer


class EducationalTransparencyAndPublicityViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalTransparencyAndPublicity.objects.all()
    serializer_class = EducationalTransparencyAndPublicitySerializer


class EducationProgramViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationProgram.objects.all()
    serializer_class = EducationProgramSerializer


class EducationProgramAccreditationInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationProgramAccreditationInformation.objects.all()
    serializer_class = EducationProgramAccreditationInformationSerializer


class EducationProgramDocumentViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationProgramDocument.objects.all()
    serializer_class = EducationProgramDocumentSerializer


class EducationProgramGeneralInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationProgramGeneralInformation.objects.all()
    serializer_class = EducationProgramGeneralInformationSerializer


class EducationStatisticsViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationStatistics.objects.all()
    serializer_class = EducationStatisticsSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class FieldOfStudyViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer


class GeneralInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = GeneralInformation.objects.all()
    serializer_class = GeneralInformationSerializer


class GeneralQuestionAnswerViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = GeneralQuestionAnswer.objects.all()
    serializer_class = GeneralQuestionAnswerSerializer


class HEILinksInEDEBOViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = HEILinksInEDEBO.objects.all()
    serializer_class = HEILinksInEDEBOSerializer


class HigherEducationInstitutionViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = HigherEducationInstitution.objects.all()
    serializer_class = HigherEducationInstitutionSerializer


class HigherEducationInstitutionAreaViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = HigherEducationInstitutionArea.objects.all()
    serializer_class = HigherEducationInstitutionAreaSerializer


class HigherEducationInstitutionInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = HigherEducationInstitutionInformation.objects.all()
    serializer_class = HigherEducationInstitutionInformationSerializer


class HumanResourcesViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = HumanResources.objects.all()
    serializer_class = HumanResourcesSerializer


class InformationOnSelfAssessmentOfEducationalProgramViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = InformationOnSelfAssessmentOfEducationalProgram.objects.all()
    serializer_class = InformationOnSelfAssessmentOfEducationalProgramSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class OtherHigherEducationProgramViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = OtherHigherEducationProgram.objects.all()
    serializer_class = OtherHigherEducationProgramSerializer


class ProgramLearningOutcomeCorrespondenceMatrixViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = ProgramLearningOutcomeCorrespondenceMatrix.objects.all()
    serializer_class = ProgramLearningOutcomeCorrespondenceMatrixSerializer


class QualityAssuranceViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = QualityAssurance.objects.all()
    serializer_class = QualityAssuranceSerializer


class SelfAssessmentEducationalProgramRestrictedInfoViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = SelfAssessmentEducationalProgramRestrictedInfo.objects.all()
    serializer_class = SelfAssessmentEducationalProgramRestrictedInfoSerializer


class SeparateStructuralUnitViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = SeparateStructuralUnit.objects.all()
    serializer_class = SeparateStructuralUnitSerializer


class SpecialtyViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class StructuralSubdivisionViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = StructuralSubdivision.objects.all()
    serializer_class = StructuralSubdivisionSerializer


class TablesAnnexViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = TablesAnnex.objects.all()
    serializer_class = TablesAnnexSerializer


class TeacherSummaryInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = TeacherSummaryInformation.objects.all()
    serializer_class = TeacherSummaryInformationSerializer
