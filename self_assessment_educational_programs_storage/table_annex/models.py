from django.db import models


# Таблиця 1. Інформація про обов’язкові освітні компоненти ОП
class EducationalProgramComponentsInformation(models.Model):
    # 1
    # TODO: check Foreign Key
    component_name = models.CharField(
        verbose_name="Назва освітнього компонента",
        help_text="Назва обов'язкового освітнього компонента",
        max_length=255,
    )
    # 2
    # TODO: check Foreign Key
    # TODO: Probably new table
    component_type = models.CharField(
        verbose_name="Вид компонента",
        help_text="Вид обов'язкового освітнього компонента",
        max_length=255,
    )
    # 3
    syllabus = models.FileField(
        verbose_name="Поле завантаження силабуса/навчально-методичних матеріалів",
        help_text="Поле для завантаження силабуса або інших навчально-методичних матеріалів",
        upload_to="syllabus/",
        max_length=255,
        blank=True,
        null=True,
    )
    # 4
    special_equipment_info = models.TextField(
        verbose_name="Інформація про спеціальне обладнання",
        help_text="Якщо освітній компонент потребує спеціального матеріально-технічного "
        "та/або інформаційного забезпечення, наведіть відомості щодо нього*",
    )

    class Meta:
        db_table = "program_educational_components_information"
        verbose_name = "Інформація про обов’язковий освітній компонент ОП"
        verbose_name_plural = "Інформація про обов’язкові освітні компоненти ОП"

    def __str__(self):
        return f"{self.component_name} {self.component_type}"


# Таблиця 2. Зведена інформація про викладачів
class TeacherSummaryInformation(models.Model):
    # 1
    teacher_full_name = models.ForeignKey(
        "users.Teacher",
        verbose_name="ПІБ викладача",
        help_text="Повне ім'я викладача",
        on_delete=models.PROTECT,
    )
    # 3
    # TODO: check Foreign Key
    structural_subdivision = models.ForeignKey(
        "general_information.StructuralSubdivision",
        on_delete=models.PROTECT,
        help_text="Структурний підрозділ, у якому працює викладач",
        related_name="structural_subdivision_teacher_information",
    )
    # 4
    teacher_qualification = models.CharField(
        max_length=200,
        verbose_name="Кваліфікація викладача",
        help_text="Інформація про кваліфікацію викладача",
    )
    # 5
    teacher_experience = models.IntegerField(
        verbose_name="Стаж роботи", help_text="Стаж науково-педагогічної роботи в роках"
    )
    # 6
    # TODO: check Foreign Key
    education_disciplines = models.TextField(
        verbose_name="Навчальні дисципліни",
        help_text="Навчальні дисципліни, що їх викладає викладач на ОП",
    )
    # 7
    rationale = models.TextField(
        verbose_name="Обґрунтування",
        help_text="Обґрунтування",
    )

    class Meta:
        db_table = "teacher_summary_information"
        verbose_name = "Зведена інформація про викладача"
        verbose_name_plural = "Зведена інформація про викладачів"

    def __str__(self):
        return f"{self.teacher_full_name} {self.structural_subdivision_id} {self.structural_subdivision}"


# Таблиця 3. Матриця відповідності програмних результатів навчання, освітніх компонентів, методів навчання, оцінювання
class ProgramLearningOutcomeCorrespondenceMatrix(models.Model):
    # 1
    educational_component = models.ForeignKey(
        "EducationalProgramComponentsInformation",
        on_delete=models.CASCADE,
        verbose_name="Освітній компонент",
        help_text="Назва освітнього компонента",
    )
    # 2
    name = models.TextField(
        max_length=3000,
        verbose_name="Результати навчання",
        help_text="Назва програмного результату навчання",
    )
    # 3
    teaching_method = models.CharField(
        max_length=1000,
        verbose_name="Методи навчання",
        help_text="Назва методу навчання",
    )
    # 4
    assessment_form = models.CharField(
        max_length=200,
        verbose_name="Форми оцінювання",
        help_text="Назва форми оцінювання",
    )

    class Meta:
        db_table = "program_learning_outcome_correspondence_matrix"
        verbose_name = (
            "Матриця відповідності програмних результатів навчання, "
            "освітніх компонентів, методів навчання та оцінювання"
        )
        verbose_name_plural = (
            "Матриця відповідності програмних результатів навчання, "
            "освітніх компонентів, методів навчання та оцінювання"
        )

    def __str__(self):
        return f"{self.educational_component} {self.name}"


# Таблиці
class TablesAnnex(models.Model):
    program_educational_components_information = models.ForeignKey(
        "EducationalProgramComponentsInformation",
        on_delete=models.PROTECT,
        related_name="components_information_tables_annex",
        verbose_name="Інформація про обов’язкові освітні компоненти ОП",
        help_text="Наводять відомості, як мінімум, щодо наявності відповідного матеріально-технічного забезпечення, "
        "його достатності для реалізації ОП; для обладнання/устаткування – також кількість, "
        "рік введення в експлуатацію, рік останнього ремонту; "
        "для програмного забезпечення – також кількість ліцензій та версія програмного забезпечення",
    )
    teacher_summary_information = models.ForeignKey(
        "TeacherSummaryInformation",
        on_delete=models.PROTECT,
        related_name="teacher_summary_information_tables_annex",
        verbose_name="Зведена інформація про викладачів",
        help_text="Обґрунтування зазначається окремо щодо кожної дисципліни, яку викладає викладач.",
    )
    program_learning_outcome_correspondence_matrix = models.ManyToManyField(
        "ProgramLearningOutcomeCorrespondenceMatrix",
        related_name="correspondence_matrix_tables_annex",
        verbose_name="Матриця відповідності програмних результатів навчання, "
        "освітніх компонентів, методів навчання та оцінювання",
        help_text="Для кожного освітнього компонента заповнюється окрема таблиця.",
    )

    class Meta:
        db_table = "table_annex"
        verbose_name = "Відповідь на загальні питання"
        verbose_name_plural = "Відповіді на загальні питання"
