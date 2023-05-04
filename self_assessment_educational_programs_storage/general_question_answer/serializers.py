"""Kissa commands serializers."""
from models import (
    ControlMeasuresAndAcademicIntegrity,
    EducationalEnvironmentAndMaterialResources,
    EducationalProgram,
    EducationalProgramAccess,
    EducationalProgramDesign,
    EducationalProgramDevelopmentPerspectives,
    EducationalProgramLearningAndTeaching,
    EducationalProgramStructureAndContent,
    EducationalTransparencyAndPublicity,
    GeneralQuestionAnswer,
    HumanResources,
    Language,
    QualityAssurance,
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


class GeneralQuestionAnswerSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = GeneralQuestionAnswer
        fields = "__all__"


class HumanResourcesSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = HumanResources
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = Language
        fields = "__all__"


class QualityAssuranceSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = QualityAssurance
        fields = "__all__"
