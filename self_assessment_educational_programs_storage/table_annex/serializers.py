"""Kissa commands serializers."""
from models import (
    EducationalProgramComponentsInformation,
    ProgramLearningOutcomeCorrespondenceMatrix,
    TablesAnnex,
    TeacherSummaryInformation,
)
from rest_framework import serializers


class EducationalProgramComponentsInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = EducationalProgramComponentsInformation
        fields = "__all__"


class TeacherSummaryInformationSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = TeacherSummaryInformation
        fields = "__all__"


class ProgramLearningOutcomeCorrespondenceMatrixSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = ProgramLearningOutcomeCorrespondenceMatrix
        fields = "__all__"


class TablesAnnexSerializer(serializers.ModelSerializer):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = TablesAnnex
        fields = "__all__"
