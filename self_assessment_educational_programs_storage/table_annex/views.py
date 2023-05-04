from rest_framework import viewsets

from .models import (
    EducationalProgramComponentsInformation,
    ProgramLearningOutcomeCorrespondenceMatrix,
    TablesAnnex,
    TeacherSummaryInformation,
)
from .serializers import (
    EducationalProgramComponentsInformationSerializer,
    ProgramLearningOutcomeCorrespondenceMatrixSerializer,
    TablesAnnexSerializer,
    TeacherSummaryInformationSerializer,
)


class EducationalProgramComponentsInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = EducationalProgramComponentsInformation.objects.all()
    serializer_class = EducationalProgramComponentsInformationSerializer


class ProgramLearningOutcomeCorrespondenceMatrixViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = ProgramLearningOutcomeCorrespondenceMatrix.objects.all()
    serializer_class = ProgramLearningOutcomeCorrespondenceMatrixSerializer


class TablesAnnexViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = TablesAnnex.objects.all()
    serializer_class = TablesAnnexSerializer


class TeacherSummaryInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = TeacherSummaryInformation.objects.all()
    serializer_class = TeacherSummaryInformationSerializer
