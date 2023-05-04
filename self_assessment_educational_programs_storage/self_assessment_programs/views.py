from rest_framework import viewsets

from .models import InformationOnSelfAssessmentOfEducationalProgram
from .serializers import InformationOnSelfAssessmentOfEducationalProgramSerializer


class InformationOnSelfAssessmentOfEducationalProgramViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = InformationOnSelfAssessmentOfEducationalProgram.objects.all()
    serializer_class = InformationOnSelfAssessmentOfEducationalProgramSerializer
