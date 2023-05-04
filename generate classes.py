classes = [
    "EducationalEnvironmentAndMaterialResources",
    "EducationalProgram",
    "EducationalProgramAccess",
    "EducationalProgramComponentsInformation",
    "EducationalProgramDesign",
    "EducationalProgramDevelopmentPerspectives",
    "EducationalProgramLearningAndTeaching",
    "EducationalProgramStructureAndContent",
    "EducationalTransparencyAndPublicity",
    "EducationProgram",
    "EducationProgramAccreditationInformation",
    "EducationProgramDocument",
    "EducationProgramGeneralInformation",
    "EducationStatistics",
    "Employee",
    "FieldOfStudy",
    "GeneralInformation",
    "GeneralQuestionAnswer",
    "HEILinksInEDEBO",
    "HigherEducationInstitution",
    "HigherEducationInstitutionArea",
    "HigherEducationInstitutionInformation",
    "HumanResources",
    "InformationOnSelfAssessmentOfEducationalProgram",
    "Language",
    "OtherHigherEducationProgram",
    "ProgramLearningOutcomeCorrespondenceMatrix",
    "QualityAssurance",
    "SelfAssessmentEducationalProgramRestrictedInfo",
    "SeparateStructuralUnit",
    "Specialty",
    "StructuralSubdivision",
    "TablesAnnex",
    "TeacherSummaryInformation",
]

print([i + "Serializer" for i in classes])

template_serializer = """
            class {class_name}Serializer(serializers.ModelSerializer):

                class Meta:

                    model = {class_name}
                    fields = "__all__"


           """

tempalate_view = """
                class {class_name}ViewSet(viewsets.ModelViewSet):
                    "123"

                    queryset = {class_name}.objects.all()
                    serializer_class = {class_name}Serializer
                """

for i in classes:
    print(tempalate_view.format(class_name=i))
