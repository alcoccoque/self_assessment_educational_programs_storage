from django.contrib import admin

from .models import (
    EducationalProgramComponentsInformation,
    ProgramLearningOutcomeCorrespondenceMatrix,
    TablesAnnex,
    TeacherSummaryInformation,
)


@admin.register(EducationalProgramComponentsInformation)
class EducationalProgramComponentsInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherSummaryInformation)
class TeacherSummaryInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramLearningOutcomeCorrespondenceMatrix)
class ProgramLearningOutcomeCorrespondenceMatrixAdmin(admin.ModelAdmin):
    pass


@admin.register(TablesAnnex)
class TablesAnnexAdmin(admin.ModelAdmin):
    pass
