"""Kissa commands serializers."""

from models import InformationOnSelfAssessmentOfEducationalProgram
from rest_framework import serializers


class InformationOnSelfAssessmentOfEducationalProgramSerializer(
    serializers.ModelSerializer
):
    """Allow to convert fields of model instance to native Python data types."""

    class Meta:
        """Meta."""

        model = InformationOnSelfAssessmentOfEducationalProgram
        fields = "__all__"
