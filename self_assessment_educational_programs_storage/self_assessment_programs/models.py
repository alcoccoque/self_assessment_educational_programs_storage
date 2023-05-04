from django.contrib.auth.models import User
from django.db import models


# Фінальна таблиця що зберігає всю інформацію по ВІДОМОСТІ ПРО САМООЦІНЮВАННЯ ОСВІТНЬОЇ ПРОГРАМИ
class InformationOnSelfAssessmentOfEducationalProgram(models.Model):
    # Part 1
    general_information = models.ForeignKey(
        "general_information.GeneralInformation",
        on_delete=models.PROTECT,
        related_name="general_information_self_assessment",
        verbose_name="Загальні відомості",
        help_text="Перша частина довідника, що містить інформацію про ЗВО та ОП",
    )
    # Part 2
    general_question_answer = models.ForeignKey(
        "general_question_answer.GeneralQuestionAnswer",
        on_delete=models.PROTECT,
        related_name="general_question_answer_self_assessment",
        verbose_name="Відповіді на загальні питання",
        help_text="Друга частина довідника, що містить відповіді на загальні питання",
    )
    # Tables
    tables_annex = models.ForeignKey(
        "table_annex.TablesAnnex",
        on_delete=models.PROTECT,
        related_name="tables_annex_self_assessment",
        verbose_name="Таблиці додаток",
        help_text="Додаток до довідника про самооцінювання ОП(таблиці)",
    )

    class Meta:
        db_table = "information_on_self_assessment_of_educational_program"
        verbose_name = "Довідник про самооцінювання ОП"
        verbose_name_plural = "Довідники про самооцінювання ОП"

    def __str__(self):
        return f"Довідник про самооцінювання ({self.pk}) - ОП: {self.general_information.education_program_accreditation_information.education_program.name}, спеціальність: {self.general_information.education_program_accreditation_information.specialty.specialty}"
