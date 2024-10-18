from django.shortcuts import redirect, render
from rest_framework import viewsets

from self_assessment_educational_programs_storage.users.parsers import (
    parse_teacher_file,
)

from .forms import TeacherFileForm, TeacherForm
from .models import (
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
    TeacherFile,
)
from .serializers import (
    EducationProgramAccreditationInformationSerializer,
    EducationProgramDocumentSerializer,
    EducationProgramGeneralInformationSerializer,
    EducationProgramSerializer,
    EducationStatisticsSerializer,
    FieldOfStudySerializer,
    GeneralInformationSerializer,
    HEILinksInEDEBOSerializer,
    HigherEducationInstitutionAreaSerializer,
    HigherEducationInstitutionInformationSerializer,
    HigherEducationInstitutionSerializer,
    OtherHigherEducationProgramSerializer,
    SelfAssessmentEducationalProgramRestrictedInfoSerializer,
    SeparateStructuralUnitSerializer,
    SpecialtySerializer,
    StructuralSubdivisionSerializer,
)


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


class FieldOfStudyViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = FieldOfStudy.objects.all()
    serializer_class = FieldOfStudySerializer


class GeneralInformationViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = GeneralInformation.objects.all()
    serializer_class = GeneralInformationSerializer


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


class OtherHigherEducationProgramViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = OtherHigherEducationProgram.objects.all()
    serializer_class = OtherHigherEducationProgramSerializer


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
