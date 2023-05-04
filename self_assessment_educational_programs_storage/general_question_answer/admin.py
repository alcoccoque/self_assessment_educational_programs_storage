from django.contrib import admin

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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalProgramDesign)
class EducationalProgramDesignAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalProgramStructureAndContent)
class EducationalProgramStructureAndContentAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalProgramAccess)
class EducationalProgramAccessAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalProgramLearningAndTeaching)
class EducationalProgramLearningAndTeachingAdmin(admin.ModelAdmin):
    pass


@admin.register(ControlMeasuresAndAcademicIntegrity)
class ControlMeasuresAndAcademicIntegrityAdmin(admin.ModelAdmin):
    pass


@admin.register(HumanResources)
class HumanResourcesAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalEnvironmentAndMaterialResources)
class EducationalEnvironmentAndMaterialResourcesAdmin(admin.ModelAdmin):
    pass


@admin.register(QualityAssurance)
class QualityAssuranceAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalTransparencyAndPublicity)
class EducationalTransparencyAndPublicityAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationalProgramDevelopmentPerspectives)
class EducationalProgramDevelopmentPerspectivesAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralQuestionAnswer)
class GeneralQuestionAnswerAdmin(admin.ModelAdmin):
    pass
