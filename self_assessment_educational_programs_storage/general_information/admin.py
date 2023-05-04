from django.contrib import admin

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
)


@admin.register(FieldOfStudy)
class FieldOfStudyAdmin(admin.ModelAdmin):
    pass


@admin.register(StructuralSubdivision)
class StructuralSubdivisionAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(HigherEducationInstitution)
class HigherEducationInstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationProgram)
class EducationProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(SeparateStructuralUnit)
class SeparateStructuralUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(HigherEducationInstitutionInformation)
class HigherEducationInstitutionInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(HEILinksInEDEBO)
class HEILinksInEDEBOAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationProgramAccreditationInformation)
class EducationProgramAccreditationInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationProgramGeneralInformation)
class EducationProgramGeneralInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationStatistics)
class EducationStatisticsAdmin(admin.ModelAdmin):
    pass


@admin.register(OtherHigherEducationProgram)
class OtherHigherEducationProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(HigherEducationInstitutionArea)
class HigherEducationInstitutionAreaAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationProgramDocument)
class EducationProgramDocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(SelfAssessmentEducationalProgramRestrictedInfo)
class SelfAssessmentEducationalProgramRestrictedInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralInformation)
class GeneralInformationAdmin(admin.ModelAdmin):
    pass
