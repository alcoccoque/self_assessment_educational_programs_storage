from rest_framework import viewsets

from .models import (
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
from .serializers import (
    ControlMeasuresAndAcademicIntegritySerializer,
    EducationalEnvironmentAndMaterialResourcesSerializer,
    EducationalProgramAccessSerializer,
    EducationalProgramDesignSerializer,
    EducationalProgramDevelopmentPerspectivesSerializer,
    EducationalProgramLearningAndTeachingSerializer,
    EducationalProgramSerializer,
    EducationalProgramStructureAndContentSerializer,
    EducationalTransparencyAndPublicitySerializer,
    GeneralQuestionAnswerSerializer,
    HumanResourcesSerializer,
    LanguageSerializer,
    QualityAssuranceSerializer,
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


class GeneralQuestionAnswerViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = GeneralQuestionAnswer.objects.all()
    serializer_class = GeneralQuestionAnswerSerializer


class HumanResourcesViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = HumanResources.objects.all()
    serializer_class = HumanResourcesSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class QualityAssuranceViewSet(viewsets.ModelViewSet):
    """Implements basic http commands: get, post, put, delete."""

    queryset = QualityAssurance.objects.all()
    serializer_class = QualityAssuranceSerializer
