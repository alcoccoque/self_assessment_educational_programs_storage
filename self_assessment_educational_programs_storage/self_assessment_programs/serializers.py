"""Kissa commands serializers."""
from models import (
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
from rest_framework import serializers


class ControlMeasuresAndAcademicIntegritySerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = ControlMeasuresAndAcademicIntegrity
        fields = "__all__"


class EducationalEnvironmentAndMaterialResourcesSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalEnvironmentAndMaterialResources
        fields = "__all__"


class EducationalProgramSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgram
        fields = "__all__"


class EducationalProgramAccessSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramAccess
        fields = "__all__"


class EducationalProgramComponentsInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramComponentsInformation
        fields = "__all__"


class EducationalProgramDesignSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramDesign
        fields = "__all__"


class EducationalProgramDevelopmentPerspectivesSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramDevelopmentPerspectives
        fields = "__all__"


class EducationalProgramLearningAndTeachingSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramLearningAndTeaching
        fields = "__all__"


class EducationalProgramStructureAndContentSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramStructureAndContent
        fields = "__all__"


class EducationalTransparencyAndPublicitySerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalTransparencyAndPublicity
        fields = "__all__"


class EducationProgramSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationProgram
        fields = "__all__"


class EducationProgramAccreditationInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationProgramAccreditationInformation
        fields = "__all__"


class EducationProgramDocumentSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationProgramDocument
        fields = "__all__"


class EducationProgramGeneralInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationProgramGeneralInformation
        fields = "__all__"


class EducationStatisticsSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationStatistics
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = Employee
        fields = "__all__"


class FieldOfStudySerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = FieldOfStudy
        fields = "__all__"


class GeneralInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = GeneralInformation
        fields = "__all__"


class GeneralQuestionAnswerSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = GeneralQuestionAnswer
        fields = "__all__"


class HEILinksInEDEBOSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = HEILinksInEDEBO
        fields = "__all__"


class HigherEducationInstitutionSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = HigherEducationInstitution
        fields = "__all__"


class HigherEducationInstitutionAreaSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = HigherEducationInstitutionArea
        fields = "__all__"


class HigherEducationInstitutionInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = HigherEducationInstitutionInformation
        fields = "__all__"


class HumanResourcesSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = HumanResources
        fields = "__all__"


class InformationOnSelfAssessmentOfEducationalProgramSerializer(
    serializers.ModelSerializer
):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = InformationOnSelfAssessmentOfEducationalProgram
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = Language
        fields = "__all__"


class OtherHigherEducationProgramSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = OtherHigherEducationProgram
        fields = "__all__"


class ProgramLearningOutcomeCorrespondenceMatrixSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = ProgramLearningOutcomeCorrespondenceMatrix
        fields = "__all__"


class QualityAssuranceSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = QualityAssurance
        fields = "__all__"


class SelfAssessmentEducationalProgramRestrictedInfoSerializer(
    serializers.ModelSerializer
):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = SelfAssessmentEducationalProgramRestrictedInfo
        fields = "__all__"


class SeparateStructuralUnitSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = SeparateStructuralUnit
        fields = "__all__"


class SpecialtySerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = Specialty
        fields = "__all__"


class StructuralSubdivisionSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = StructuralSubdivision
        fields = "__all__"


class TablesAnnexSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = TablesAnnex
        fields = "__all__"


class TeacherSummaryInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = TeacherSummaryInformation
        fields = "__all__"
