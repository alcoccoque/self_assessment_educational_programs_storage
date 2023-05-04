from django.contrib import admin

from .models import InformationOnSelfAssessmentOfEducationalProgram


@admin.register(InformationOnSelfAssessmentOfEducationalProgram)
class InformationOnSelfAssessmentOfEducationalProgramAdmin(admin.ModelAdmin):
    pass
