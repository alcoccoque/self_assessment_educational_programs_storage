from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Answer(models.IntegerChoices):
    NO = 0, _("Ні")
    YES = 1, _("Так")

    __empty__ = _("(Невідомо)")


class FieldOfStudy(models.Model):
    field_of_study_code = models.IntegerField(
        verbose_name="Код галузі знань", help_text="Код галузі знань"
    )
    field_of_study = models.CharField(
        max_length=250, verbose_name="Галузь знань", help_text="Галузь знань"
    )

    class Meta:
        db_table = "field_of_study"
        verbose_name = "Галузь знань"
        verbose_name_plural = "Галузі знань"

    def __str__(self):
        return f"{self.field_of_study_code} {self.field_of_study}"


class Specialty(models.Model):
    specialty_code = models.IntegerField(
        verbose_name="Код спеціальності", help_text="Код спеціальності"
    )
    specialty = models.CharField(
        max_length=250, verbose_name="Спеціальність", help_text="Спеціальність"
    )

    class Meta:
        db_table = "specialty"
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __str__(self):
        return f"{self.specialty_code} {self.specialty}"


class StructuralSubdivision(models.Model):
    responsible_department = models.CharField(
        max_length=255,
        verbose_name="Структурний підрозділ",
        help_text="Структурний підрозділ (кафедра або інший підрозділ), відповідальний за реалізацію ОП",
    )

    class Meta:
        db_table = "structural_subdivision"
        verbose_name = "Структурний підрозділ"
        verbose_name_plural = "Структурні підрозділи"

    def __str__(self):
        return f"{self.responsible_department}"


class HigherEducationInstitution(models.Model):
    # Row 1
    hei_id = models.BigIntegerField(
        verbose_name="Реєстраційний номер у ЄДЕБО",
        help_text="Реєстраційний номер ЗВО у ЄДЕБО",
    )
    # Row 2
    higher_educational_institution_name = models.CharField(
        max_length=250, verbose_name="Повна назва", help_text="Повна назва ЗВО"
    )
    # Row 3
    institution_code = models.BigIntegerField(
        verbose_name="Ідентифікаційний код",
        help_text="Ідентифікаційний код ЗВО",
    )
    # Row 4
    head_full_name = models.ForeignKey(
        "users.Teacher",
        verbose_name="ПІБ керівника",
        help_text="ПІБ керівника ЗВО",
        on_delete=models.PROTECT,
    )
    # Row 5
    website = models.URLField(
        verbose_name="Посилання на офіційний вебсайт",
        help_text="Посилання на офіційний вебсайт ЗВО",
    )

    class Meta:
        db_table = "higher_educational_institution"
        verbose_name = "Загальна відомість про заклад вищої освіти"
        verbose_name_plural = "Загальні відомості про заклад вищої освіти"

    def __str__(self):
        return f"{self.hei_id} {self.higher_educational_institution_name}"


class EducationProgram(models.Model):
    # Row 1
    education_program_id = models.BigIntegerField(
        verbose_name="ID освітньої програми",
        help_text="ID освітньої програми в ЄДЕБО",
    )
    # Row 2
    name = models.CharField(
        max_length=250, verbose_name="Назва ОП", help_text="Назва ОП"
    )

    class Meta:
        db_table = "education_program"
        verbose_name = "Освітня програма"
        verbose_name_plural = "Освітні програми"

    def __str__(self):
        return f"{self.education_program_id} {self.name}"


# Інформація про відокремлений структурний підрозділ (ВСП) (зазначається лише якщо ОП реалізується у ВСП)
class SeparateStructuralUnit(models.Model):
    # Row 6
    ssu_id = models.BigIntegerField(
        verbose_name="Реєстраційний номер ВСП у ЄДЕБО",
        help_text="Реєстраційний номер ВСП ЗВО у ЄДЕБО",
    )
    # Row 7
    # institution = models.ForeignKey(
    #     HigherEducationInstitution,
    #     on_delete=models.CASCADE,
    #     verbose_name="ЗВО",
    #     help_text="ЗВО",
    # )
    # Row 7
    separate_structural_unit_name = models.CharField(
        max_length=250, verbose_name="Повна назва", help_text="Повна назва ВСП ЗВО"
    )
    # Row 8
    ssu_code = models.BigIntegerField(
        verbose_name="Ідентифікаційний код",
        help_text="Ідентифікаційний код ВСП ЗВО",
    )
    # Row 9
    head_full_name = models.ForeignKey(
        "users.Teacher",
        verbose_name="ПІБ керівника",
        help_text="ПІБ керівника ВСП ЗВО",
        on_delete=models.PROTECT,
    )
    # Row 10
    website = models.URLField(
        verbose_name="Посилання на офіційний вебсайт",
        help_text="Посилання на офіційний вебсайт ВСП ЗВО",
    )

    class Meta:
        db_table = "separate_structural_unit"
        verbose_name = "Інформація про відокремлений структурний підрозділ (ВСП)"
        verbose_name_plural = "Інформація про відокремлений структурний підрозділ (ВСП)"


# 1. Інформація про заклад вищої освіти
class HigherEducationInstitutionInformation(models.Model):
    hei = models.ForeignKey(
        "HigherEducationInstitution",
        on_delete=models.PROTECT,
        verbose_name="Заклад вищої освіти",
        help_text="Інформація про заклад вищої освіти",
    )
    ssu = models.ForeignKey(
        "SeparateStructuralUnit",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Відокремлений структурний підрозділ",
        help_text="Інформація про відокремлений структурний підрозділ",
    )

    class Meta:
        db_table = "higher_education_institution_information"
        verbose_name = "Інформація про заклад вищої освіти"
        verbose_name_plural = "Інформація про заклади вищої освіти"


# 2. Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО
class HEILinksInEDEBO(models.Model):
    website = models.URLField(
        verbose_name="Посилання на інформацію про ЗВО у Реєстрі ЄДЕБО",
        help_text="Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
    )

    class Meta:
        db_table = "hei_links_in_edebo"
        verbose_name = "Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО"
        verbose_name_plural = "Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО"

    def __str__(self):
        return f"{self.website}"


# 3. Загальна інформація про освітню програму, яка подається на акредитацію
class EducationProgramAccreditationInformation(models.Model):
    # Row 1 Row 2
    education_program = models.ForeignKey(
        "EducationProgram",
        on_delete=models.PROTECT,
        related_name="education_program_accreditation_information",
    )
    # Row 3
    specialty_licensing_info = models.CharField(
        max_length=250,
        verbose_name="Реквізити рішення про ліцензування спеціальності",
        help_text="Реквізити рішення про ліцензування спеціальності на відповідному рівні вищої освіти",
    )
    # Row 4
    cycle = models.CharField(
        max_length=250, verbose_name="Цикл", help_text="Цикл (рівень вищої освіти)"
    )
    # Row 5
    field_of_study = models.ForeignKey(
        "FieldOfStudy",
        on_delete=models.PROTECT,
        verbose_name="Галузь знань",
        help_text="Галузь знань",
    )
    # Row 6
    specialty = models.ForeignKey(
        "Specialty",
        on_delete=models.PROTECT,
        verbose_name="Спеціальність",
        help_text="Спеціальність",
    )
    # Row 7
    specialization = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Спеціалізація",
        help_text="Спеціалізація",
    )
    # Row 8
    program_type = models.CharField(
        max_length=250,
        verbose_name="Вид освітньої програми",
        help_text="Вид освітньої програми",
    )
    # Row 9
    admission_degree = models.CharField(
        max_length=250,
        verbose_name="Основний ступень",
        help_text="Вступ на освітню програму здійснюється на основі ступеня (рівня)",
    )
    # Row 10
    duration = models.CharField(
        max_length=255,
        verbose_name="Термін навчання",
        help_text="Термін навчання на освітній програмі",
    )
    # Row 11
    education_program_forms = models.CharField(
        max_length=255,
        verbose_name="Форми здобуття освіти",
        help_text="Форми здобуття освіти на ОП",
    )
    # Row 12
    structural_subdivision = models.ForeignKey(
        "StructuralSubdivision",
        on_delete=models.PROTECT,
        verbose_name="Структурний підрозділ відповідальний за реалізацію ОП",
        help_text="Структурний підрозділ (кафедра або інший підрозділ), відповідальний за реалізацію ОП",
        related_name="structural_subdivision_ep_accreditation",
    )
    # Row 13
    other_educational_structural_subdivisions = models.ManyToManyField(
        "StructuralSubdivision",
        verbose_name="Інші навчальні структурні підрозділи",
        help_text="Інші навчальні структурні підрозділи (кафедра або інші підрозділи), залучені до реалізації ОП",
        related_name="other_structural_subdivision_ep_accreditation",
    )
    # Row 14
    location = models.CharField(
        max_length=255,
        verbose_name="Місце провадження освітньої діяльності",
        help_text="Місце (адреса) провадження освітньої діяльності за ОП",
    )
    # Row 15
    grants_professional_qualification = models.IntegerField(
        choices=Answer.choices,
        verbose_name="Присвоєння професійної кваліфікації ОП",
        help_text="Освітня програма передбачає присвоєння професійної кваліфікації",
    )
    # Row 16
    professional_qualification = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Професійна кваліфікація",
        help_text="Професійна кваліфікація, яка присвоюється за ОП (за наявності)",
    )
    # Row 17
    language_of_instruction = models.ManyToManyField(
        "general_question_answer.Language",
        verbose_name="Мова викладання",
        help_text="Мова (мови) викладання",
    )
    # Row 18
    guarantee_id = models.BigIntegerField(
        verbose_name="ID гаранта у ЄДЕБО",
        help_text="ID гаранта ОП у ЄДЕБО",
    )
    # Row 19
    guarantee_full_name = models.ForeignKey(
        "users.Teacher",
        verbose_name="ПІБ гаранта",
        help_text="ПІБ гаранта ОП",
        on_delete=models.PROTECT,
    )
    # Row 20
    guarantee_position = models.CharField(
        max_length=255, verbose_name="Посада гаранта", help_text="Посада гаранта ОП"
    )
    # Row 21
    guarantee_email = models.EmailField(
        verbose_name="Корпоративна електронна адреса гаранта",
        help_text="Корпоративна електронна адреса гаранта ОП",
    )
    # Row 22
    guarantee_phone = models.CharField(
        max_length=20,
        verbose_name="Контактний телефон гаранта",
        help_text="Контактний телефон гаранта ОП",
    )
    # Row 23
    additional_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Додатковий контактний телефон гаранта",
        help_text="Додатковий контактний телефон гаранта ОП",
    )

    class Meta:
        db_table = "education_program_accreditation_information"
        verbose_name = (
            "Загальна інформація про освітню програму, яка подається на акредитацію"
        )
        verbose_name_plural = (
            "Загальна інформація про освітні програми, які подаються на акредитацію"
        )


# 4. Загальні відомості про ОП, історію її розроблення та впровадження
class EducationProgramGeneralInformation(models.Model):
    history_and_development = models.TextField(
        max_length=3000,
        verbose_name="Загальні відомості про ОП",
        help_text="Загальні відомості про ОП, історію її розроблення та впровадження",
    )

    class Meta:
        db_table = "education_program_general_information"
        verbose_name = "Загальні відомості про освітню програму(ОП), історію її розроблення та впровадження"
        verbose_name_plural = "Загальні відомості про освітні програми(ОП), історію їх розроблення та впровадження"


# TODO: CHECK THIS TABLE
# 5. Інформація про контингент здобувачів вищої освіти на ОП станом на 1 жовтня поточного НР та набір на ОП
class EducationStatistics(models.Model):
    # Table columns
    class StudyCourseYear(models.IntegerChoices):
        FIRST = 1, _("1 рік навчання")
        SECOND = 2, _("2 рік навчання")
        THIRD = 3, _("3 рік навчання")
        FOURTH = 4, _("4 рік навчання")

    study_course_year = models.IntegerField(
        choices=StudyCourseYear.choices,
        verbose_name="Рік навчання",
        help_text="Рік навчання",
    )
    # Row 1
    academic_year = models.CharField(
        max_length=11,
        verbose_name="Навчальний рік",
        help_text="Навчальний рік, у якому відбувся набір здобувачів відповідного року навчання",
    )
    # Row 2
    enrollment = models.PositiveIntegerField(
        verbose_name="Обсяг набору", help_text="Обсяг набору на ОП"
    )
    # Row 3.1
    full_time = models.PositiveIntegerField(
        verbose_name="Очна форма", help_text="Очна форма навчання"
    )
    # Row 3.2
    part_time = models.PositiveIntegerField(
        verbose_name="Заочна форма", help_text="Заочна форма навчання"
    )
    # Row 4.1
    foreign_full_time = models.PositiveIntegerField(
        verbose_name="Іноземці, очна форма", help_text="Іноземці, очна форма навчання"
    )
    # Row 4.2
    foreign_part_time = models.PositiveIntegerField(
        verbose_name="Іноземці, заочна форма",
        help_text="Іноземці, заочна форма навчання",
    )

    class Meta:
        db_table = "education_statistics"
        verbose_name_plural = (
            "Інформація про контингент здобувачів вищої освіти на ОП "
            "станом на 1 жовтня поточного навчального року та набір на ОП"
        )

    def __str__(self):
        return f"{self.academic_year} навчальний рік, {self.study_course_year} рік навчання"


# 6. Інформація про інші освітні програми ЗВО за відповідною спеціальністю
class OtherHigherEducationProgram(models.Model):
    class Level(models.TextChoices):
        ENTRY = "entry", _("Початковий рівень (короткий цикл) вищої освіти")
        FIRST = "first", _("Перший (бакалаврський) рівень")
        SECOND = "second", _("Другий (магістерський) рівень")
        THIRD = "third", _("Третій (освітньонауковий/освітньотворчий) рівень")

    level = models.CharField(max_length=20, choices=Level.choices)
    education_program = models.ManyToManyField(
        EducationProgram, related_name="other_higher_education_program"
    )

    class Meta:
        db_table = "other_higher_education_program"
        verbose_name = (
            "Інформація про іншу освітню програму ЗВО за відповідною спеціальністю"
        )
        verbose_name_plural = (
            "Інформація про інші освітні програми ЗВО за відповідною спеціальністю"
        )

    def __str__(self):
        return f"{self.level} - {self.education_program}"


# 7. Інформація про площі ЗВО, станом на момент подання відомостей про самооцінювання, кв. м.
class HigherEducationInstitutionArea(models.Model):
    # Table columns
    class Area(models.TextChoices):
        GENERAL_AREA = "GA", _("Загальна площа")
        EDUCATIONAL_AREA = "EA", _("Навчальна площа")

    area_type = models.CharField(
        max_length=2,
        choices=Area.choices,
        verbose_name="Тип площі",
    )
    # 1
    all_rooms = models.BigIntegerField(
        verbose_name="Усі приміщення", help_text="Усі приміщення ЗВО"
    )
    # 2
    own_rooms = models.BigIntegerField(
        verbose_name="Власні приміщення",
        help_text="Власні приміщення ЗВО (на праві власності, господарського відання або оперативного управління)",
    )
    # 3
    other_rights_rooms = models.BigIntegerField(
        verbose_name="Приміщення з іншим правом власності",
        help_text="Приміщення, які використовуються на іншому праві, аніж право власності, "
        "господарського відання або оперативного управління (оренда, безоплатне користування тощо)",
    )
    # 4
    rented_rooms = models.BigIntegerField(
        verbose_name="Приміщення, здані в оренду",
        help_text="Приміщення, здані в оренду",
    )

    class Meta:
        db_table = "higher_education_institution_area"
        verbose_name = "Інформація про площу ЗВО, станом на момент подання відомостей про самооцінювання, кв. м"
        verbose_name_plural = "Інформація про площі ЗВО, станом на момент подання відомостей про самооцінювання, кв. м"

    def __str__(self):
        return f"{self.area_type} - {self.all_rooms}"


# 8. Поля для завантаження документів щодо ОП
class EducationProgramDocument(models.Model):
    # 1
    education_program_doc = models.FileField(
        upload_to="education_program/education_program/",
        verbose_name="Освітня програма",
        help_text="Освітня програма",
    )
    # 2
    curriculum_doc = models.FileField(
        upload_to="education_program/curriculum/",
        verbose_name="Навчальний план",
        help_text="Навчальний план за ОП",
    )
    # 3
    reviews = models.FileField(
        blank=True,
        null=True,
        upload_to="education_program/reviews/",
        verbose_name="Рецензії, відгуки роботодавців",
        help_text="Рецензії та відгуки роботодавців",
    )

    class Meta:
        db_table = "education_program_document"
        verbose_name_plural = "Поля для завантаження документів щодо ОП"

    def __str__(self):
        return f"{self.education_program_doc} - {self.curriculum_doc}"


# TODO : add this info
# 9. Інформація про наявність в акредитаційній справі інформації з обмеженим доступом
# Справа містить інформацію з обмеженим доступом – так/ні
class SelfAssessmentEducationalProgramRestrictedInfo(models.Model):
    # 1
    info_description = models.TextField(
        verbose_name="Частина відомостей з обмеженим доступом",
        help_text="Частина відомостей про самооцінювання, яка містить інформацію з обмеженим доступом",
    )
    # 2
    info_access_restriction_type = models.TextField(
        verbose_name="Вид інформації з обмеженим доступом",
        help_text="Вид інформації з обмеженим доступом",
    )
    # 3
    restricted_info_description = models.TextField(
        verbose_name="Опис інформації з обмеженим доступом",
        help_text="Опис інформації, доступ до якої обмежений",
    )
    # 4
    restricting_access_grounds = models.TextField(
        verbose_name="Підстава для обмеження доступу",
        help_text="Підстава для обмеження доступу до інформації",
    )

    class Meta:
        db_table = "self_assessment_educational_program_restricted_info"
        verbose_name = "Інформація про наявність в акредитаційній справі інформації з обмеженим доступом"
        verbose_name_plural = "Інформація про наявність в акредитаційній справі інформації з обмеженим доступом"

    def __str__(self):
        return f"{self.info_access_restriction_type}"


# Загальні відомості
class GeneralInformation(models.Model):
    # 1
    higher_education_institution_information = models.ForeignKey(
        "HigherEducationInstitutionInformation",
        on_delete=models.PROTECT,
        verbose_name="Заклад вищої освіти",
        help_text="Інформація про заклад вищої освіти",
    )
    # 2
    hei_links_in_edebo = models.ForeignKey(
        "HEILinksInEDEBO",
        on_delete=models.PROTECT,
        verbose_name="Посилання на інформацію про ЗВО у Реєстрі ЄДЕБО",
        help_text="Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
    )
    # 3
    education_program_accreditation_information = models.ForeignKey(
        "EducationProgramAccreditationInformation",
        on_delete=models.PROTECT,
        related_name="education_program_general_information",
        verbose_name="Загальна інформація про освітню програму, яка подається на акредитацію",
        help_text="Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
    )
    # 4
    education_program_general_information = models.ForeignKey(
        "EducationProgramGeneralInformation",
        on_delete=models.PROTECT,
        verbose_name="Загальні відомості про ОП",
    )
    # 5
    education_statistics = models.ForeignKey(
        "EducationStatistics",
        on_delete=models.PROTECT,
        verbose_name="Інформація про контингент здобувачів вищої освіти",
        help_text="Інформація про контингент здобувачів вищої освіти на ОП станом на 1 жовтня поточного НР та набір на ОП",
    )
    # 6
    other_higher_education_program = models.ForeignKey(
        "OtherHigherEducationProgram",
        on_delete=models.PROTECT,
        verbose_name="Інформація про інші освітні програми ЗВО за відповідною спеціальністю",
    )
    # 7
    higher_education_institution_area = models.ForeignKey(
        "HigherEducationInstitutionArea",
        on_delete=models.PROTECT,
        verbose_name="Інформація про площі ЗВО, станом на момент подання відомостей про самооцінювання",
    )
    # 8
    education_program_document = models.ForeignKey(
        "EducationProgramDocument",
        on_delete=models.PROTECT,
        verbose_name="Поля для завантаження документів щодо ОП",
    )
    # 9
    self_assessment_educational_program_restricted_info = models.ForeignKey(
        "SelfAssessmentEducationalProgramRestrictedInfo",
        on_delete=models.PROTECT,
        verbose_name="Інформація про наявність в акредитаційній справі інформації з обмеженим доступом",
    )

    class Meta:
        db_table = "general_information"
        verbose_name = "Загальна відомость"
        verbose_name_plural = "Загальні відомості"
