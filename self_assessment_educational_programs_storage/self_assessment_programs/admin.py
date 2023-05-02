from django.contrib import admin

from .models import (
    ControlMeasuresAndAcademicIntegrity,
    EducationalEnvironmentAndMaterialResources,
    EducationalProgram,
    EducationalProgramAccess,
    EducationalProgramComponentsInformation,
    EducationalProgramDesign,
    EducationalProgramDevelopmentPerspectives,
    EducationalProgramLearningAndTeaching,
    EducationalProgramStructureAndContent,
    EducationalTransparencyAndPublicity,
    EducationProgram,
    EducationProgramAccreditationInformation,
    EducationProgramDocument,
    EducationProgramGeneralInformation,
    EducationStatistics,
    Employee,
    FieldOfStudy,
    GeneralInformation,
    GeneralQuestionAnswer,
    HEILinksInEDEBO,
    HigherEducationInstitution,
    HigherEducationInstitutionArea,
    HigherEducationInstitutionInformation,
    HumanResources,
    InformationOnSelfAssessmentOfEducationalProgram,
    Language,
    OtherHigherEducationProgram,
    ProgramLearningOutcomeCorrespondenceMatrix,
    QualityAssurance,
    SelfAssessmentEducationalProgramRestrictedInfo,
    SeparateStructuralUnit,
    Specialty,
    StructuralSubdivision,
    TablesAnnex,
    TeacherSummaryInformation,
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
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


@admin.register(EducationalProgramComponentsInformation)
class EducationalProgramComponentsInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherSummaryInformation)
class TeacherSummaryInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramLearningOutcomeCorrespondenceMatrix)
class ProgramLearningOutcomeCorrespondenceMatrixAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralInformation)
class GeneralInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneralQuestionAnswer)
class GeneralQuestionAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(TablesAnnex)
class TablesAnnexAdmin(admin.ModelAdmin):
    pass


@admin.register(InformationOnSelfAssessmentOfEducationalProgram)
class InformationOnSelfAssessmentOfEducationalProgramAdmin(admin.ModelAdmin):
    pass
