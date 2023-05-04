"""Kissa commands serializers."""
from models import (
    EducationProgram,
    EducationProgramAccreditationInformation,
    EducationProgramDocument,
    EducationProgramGeneralInformation,
    EducationStatistics,
    FieldOfStudy,
    GeneralInformation,
    HEILinksInEDEBO,
    HigherEducationInstitution,
    HigherEducationInstitutionArea,
    HigherEducationInstitutionInformation,
    OtherHigherEducationProgram,
    SelfAssessmentEducationalProgramRestrictedInfo,
    SeparateStructuralUnit,
    Specialty,
    StructuralSubdivision,
)
from rest_framework import serializers


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


class OtherHigherEducationProgramSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = OtherHigherEducationProgram
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
