from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True, verbose_name="День народження")
    phone_number = models.CharField(
        max_length=15, blank=True, verbose_name="Номер телефона"
    )
    address = models.CharField(
        max_length=255, blank=True, verbose_name="Домашня адреса"
    )

    class Meta:
        abstract = True


class Student(UserProfile):
    class StudentType(models.TextChoices):
        BACHELOR = 1, _("Бакалавр")
        MASTER = 2, _("Магістр")
        POSTGRADUATE = 3, _("Аспірант")

    student_id = models.CharField(
        max_length=15, verbose_name="Унікальний номер у системі", unique=True
    )
    enrollment_date = models.DateField(
        verbose_name="Дата вступу в заклад освіти",
    )
    student_type = models.IntegerField(
        choices=StudentType.choices,
        verbose_name="Освітній ступінь",
    )

    class Meta:
        db_table = "student"
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"


class Teacher(UserProfile):
    teacher_id = models.CharField(
        max_length=15, verbose_name="Унікальний номер у системі", unique=True
    )
    hire_date = models.DateField(
        verbose_name="Дата прийняття на роботу",
    )
    department = models.ManyToManyField(
        "StructuralSubdivision",
        verbose_name="Структурний підрозділ",
        help_text="Структурний підрозділ (кафедра або інший підрозділ), відповідальний за реалізацію ОП",
    )

    class Meta:
        db_table = "Teacher"
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


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
        "Teacher",
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


class Language(models.Model):
    # Row 1
    name = models.CharField(
        max_length=50,
        verbose_name="Мова",
        help_text="Назва мови",
    )
    # Row 2
    short_name = models.CharField(
        max_length=250, verbose_name="Код мови", help_text="Скорочення від повної назви"
    )

    class Meta:
        db_table = "language"
        verbose_name = "Мова"
        verbose_name_plural = "Мови"


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
        "Teacher",
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
        db_table = "separate_structural_unit"
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
    field_of_study = models.ForeignKey("FieldOfStudy", on_delete=models.PROTECT)
    # Row 6
    specialty = models.ForeignKey("Specialty", on_delete=models.PROTECT)
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
    grants_professional_qualification = models.CharField(
        max_length=10,
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
    language_of_instruction = models.CharField(
        max_length=255,
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
        "Teacher",
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
    class StudyCourseYear(models.TextChoices):
        FIRST = 1, _("1 рік навчання")
        SECOND = 2, _("2 рік навчання")
        THIRD = 3, _("3 рік навчання")
        FOURTH = 4, _("4 рік навчання")

    study_course_year = models.PositiveSmallIntegerField(
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


# 1. Проектування та цілі освітньої програми
class EducationalProgramDesign(models.Model):
    # 1
    goals = models.TextField(
        max_length=1500,
        verbose_name="Цілі ОП",
        help_text="Якими є цілі ОП? У чому полягають особливості (унікальність) цієї програми? ",
    )
    # 2
    uniqueness = models.TextField(
        max_length=3000,
        verbose_name="Відповідність ОП до місії та стратегії ЗВО",
        help_text="Продемонструйте, із посиланням на конкретні документи ЗВО, "
        "що цілі ОП відповідають місії та стратегії ЗВО",
    )
    # 3
    stakeholder_student = models.TextField(
        max_length=1500,
        verbose_name="Врахування інтересів стейкхолдерів для здобувачів",
        help_text="Опишіть, яким чином інтереси та пропозиції таких груп заінтересованих сторін (стейкхолдерів) "
        "були враховані під час формулювання цілей та програмних результатів навчання ОП "
        "для здобувачів вищої освіти та випускників програми",
    )
    # 4
    stakeholder_employer = models.TextField(
        max_length=1500,
        verbose_name="Врахування інтересів стейкхолдерів для роботодавців",
        help_text="Опишіть, яким чином інтереси та пропозиції таких груп заінтересованих сторін (стейкхолдерів) "
        "були враховані під час формулювання цілей та програмних результатів навчання ОП "
        "для роботодавців",
    )
    # 5
    stakeholder_academic = models.TextField(
        max_length=1500,
        verbose_name="Врахування інтересів стейкхолдерів для академічної спільноти",
        help_text="Опишіть, яким чином інтереси та пропозиції таких груп заінтересованих сторін (стейкхолдерів) "
        "були враховані під час формулювання цілей та програмних результатів навчання ОП "
        "для академічної спільноти",
    )
    # 6
    stakeholder_other = models.TextField(
        max_length=1500,
        verbose_name="Врахування інтересів стейкхолдерів для інших стейкхолдерів",
        help_text="Опишіть, яким чином інтереси та пропозиції таких груп заінтересованих сторін (стейкхолдерів) "
        "були враховані під час формулювання цілей та програмних результатів навчання ОП "
        "для інших стейкхолдерів",
    )
    # 7
    market_trends = models.TextField(
        max_length=1500,
        verbose_name="Тенденції розвитку спеціальності та ринку праці",
        help_text="Продемонструйте, яким чином цілі та програмні результати навчання ОП "
        "відбивають тенденції розвитку спеціальності та ринку праці",
    )
    # 8
    industry_and_regional_context = models.TextField(
        max_length=1500,
        verbose_name="Врахування галузевого та регіонального контексту",
        help_text="Продемонструйте, яким чином під час формулювання цілей та програмних результатів навчання ОП "
        "було враховано галузевий та регіональний контекст",
    )
    # 9
    domestic_and_foreign_programs_experience = models.TextField(
        max_length=1500,
        verbose_name="Врахування досвіду аналогічних вітчизняних та іноземних програм",
        help_text="Продемонструйте, яким чином під час формулювання цілей та програмних результатів навчання ОП "
        "було враховано досвід аналогічних вітчизняних та іноземних програм",
    )
    # 10
    learning_experience_achieve = models.TextField(
        max_length=3000,
        verbose_name="Як ОП дозволяє досягти результатів навчання",
        help_text="Продемонструйте, яким чином ОП дозволяє досягти результатів навчання, "
        "визначених стандартом вищої освіти за відповідною спеціальністю та рівнем вищої освіти "
        "(за наявності)",
    )
    # 11
    national_qualifications_level = models.TextField(
        max_length=3000,
        verbose_name="Відповідність результатів ОП до рамки кваліфікацій при відсутності стандарту вищої освіти",
        help_text="Якщо стандарт вищої освіти за відповідною спеціальністю та рівнем вищої освіти відсутній, "
        "поясніть, яким чином визначені ОП програмні результати навчання відповідають вимогам "
        "Національної рамки кваліфікацій для відповідного кваліфікаційного рівня? ",
    )

    class Meta:
        db_table = "education_program_design"
        verbose_name = "Проектування та цілі освітньої програми"
        verbose_name_plural = "Проектування та цілі освітніх програми"


# 2. Структура та зміст освітньої програми
class EducationalProgramStructureAndContent(models.Model):
    # 1
    ep_credits_amount = models.PositiveIntegerField(
        verbose_name="Обсяг ОП (у кредитах ЄКТС)",
        help_text="Яким є обсяг ОП (у кредитах ЄКТС)?",
    )

    # 2
    components_credits_amount = models.PositiveSmallIntegerField(
        verbose_name="Обсяг кредитів для формування компетентностей",
        help_text="Яким є обсяг освітніх компонентів (у кредитах ЄКТС), спрямованих на формування компетентностей, "
        "визначених стандартом вищої освіти за відповідною спеціальністю "
        "та рівнем вищої освіти (за наявності)?",
    )

    # 3
    student_electives_credits_amount = models.PositiveSmallIntegerField(
        verbose_name="Обсяг кредитів відведених на дисципліни",
        help_text="Який обсяг (у кредитах ЄКТС) відводиться на дисципліни за вибором здобувачів вищої освіти?",
    )

    # 4
    content_compliance = models.TextField(
        verbose_name="Відповідність предметній області спеціальності",
        help_text="Продемонструйте, що зміст ОП відповідає предметній області заявленої для неї спеціальності "
        "(спеціальностям, якщо освітня програма є міждисциплінарною)",
        max_length=3000,
    )

    # 5
    individual_learning_path = models.TextField(
        verbose_name="Забезпечення індивідуальної освітньої траєкторії",
        help_text="Яким чином здобувачам вищої освіти забезпечена "
        "можливість формування індивідуальної освітньої траєкторії?",
        max_length=1500,
    )

    # 6
    student_choice_right = models.TextField(
        verbose_name="Право здобувачів на вибір навчальних дисциплін",
        help_text="Яким чином здобувачі вищої освіти можуть реалізувати своє право на вибір навчальних дисциплін?",
        max_length=3000,
    )

    # 7
    student_practical_training = models.TextField(
        verbose_name="Практична підготовка здобувачів",
        help_text="Опишіть, яким чином ОП та навчальний план передбачають практичну підготовку "
        "здобувачів вищої освіти, яка дозволяє здобути компетентності, "
        "необхідні для подальшої професійної діяльності",
        max_length=1500,
    )
    # 8
    student_soft_skills = models.TextField(
        verbose_name="Соціальні навички здобувачів",
        help_text="Продемонструйте, що ОП дозволяє забезпечити набуття здобувачами вищої освіти соціальних навичок "
        "(soft skills) упродовж періоду навчання, які відповідають цілям та результатам навчання ОП",
        max_length=1500,
    )
    # 9
    relevant_professional_standard = models.TextField(
        verbose_name="Вимоги професійного стандарту",
        help_text="Яким чином зміст ОП ураховує вимоги відповідного професійного стандарту?",
        max_length=1500,
    )
    # 10
    components_scope_correlating_approach = models.TextField(
        verbose_name="Підхід для співвіднесення обсягу компонентів ОП",
        help_text="Який підхід використовує ЗВО для співвіднесення обсягу окремих освітніх компонентів ОП "
        "(у кредитах ЄКТС) із фактичним навантаженням здобувачів вищої освіти "
        "(включно із самостійною роботою)?",
        max_length=1500,
    )
    # 11
    dual_form_education_structure = models.TextField(
        verbose_name="Структура ОП за дуальною формою освіти",
        help_text="Якщо за ОП здійснюється підготовка здобувачів вищої освіти за дуальною формою освіти, "
        "продемонструйте, яким чином структура освітньої програми та навчальний план "
        "зумовлюються завданнями та особливостями цієї форми здобуття освіти",
        max_length=1500,
    )


# 3. Доступ до освітньої програми та визнання результатів навчання
class EducationalProgramAccess(models.Model):
    # Paragraph 1
    admission_rules_link = models.URLField(
        verbose_name="Посилання на правила прийому",
        help_text="Наведіть посилання на веб-сторінку, яка містить інформацію про правила прийому на навчання "
        "та вимоги до вступників ОП",
    )
    # Paragraph 2
    admission_requirements = models.TextField(
        verbose_name="Вимоги до вступників та їх урахування особливостей ОП",
        help_text="Поясніть, як правила прийому на навчання та вимоги до вступників ураховують особливості ОП?",
        max_length=1500,
    )
    # Paragraph 3
    recognition_of_education_results_accessibility = models.TextField(
        verbose_name="Доступність документа про визнання результатів навчання",
        help_text="Яким документом ЗВО регулюється питання визнання результатів навчання, "
        "отриманих в інших ЗВО? Яким чином забезпечується його доступність для "
        "учасників освітнього процесу?",
        max_length=1500,
    )
    # Paragraph 4
    admission_requirements_applying_rules_practice = models.TextField(
        verbose_name="Практика застосування вказаних правил",
        help_text="Опишіть на конкретних прикладах практику застосування вказаних правил "
        "на відповідній ОП (якщо такі були)?",
        max_length=1500,
    )
    # Paragraph 5
    recognition_of_education_results_doc = models.TextField(
        verbose_name="Документ, що регулює визнання результатів навчання",
        help_text="Яким документом ЗВО регулюється питання визнання результатів навчання, "
        "отриманих у неформальній освіті? Яким чином забезпечується його доступність "
        "для учасників освітнього процесу?",
        max_length=1500,
    )
    # Paragraph 6
    education_results_doc_applying_rules_practice = models.TextField(
        verbose_name="Практика застосування вказаних правил",
        help_text="Опишіть на конкретних прикладах практику застосування вказаних правил "
        "на відповідній ОП (якщо такі були)?",
        max_length=1500,
    )

    class Meta:
        db_table = "educational_program_access"
        verbose_name = "Доступ до освітньої програми, результатів навчання"
        verbose_name_plural = "Доступ до освітніх програм, результатів навчання"


# 4 Навчання і викладання за освітньою програмою
class EducationalProgramLearningAndTeaching(models.Model):
    # Paragraph 1
    learning_and_teaching_methods = models.TextField(
        verbose_name="Документи, що сприяють досягненню програмних результатів навчання",
        help_text="Продемонструйте, яким чином форми та методи навчання і викладання на ОП "
        "сприяють досягненню програмних результатів навчання? "
        "Наведіть посилання на відповідні документи",
        max_length=1500,
    )

    # Paragraph 2
    student_centered_approach = models.TextField(
        verbose_name="Вимоги студентоцентрованого підходу",
        help_text="Продемонструйте, яким чином форми і методи навчання і викладання відповідають вимогам "
        "студентоцентрованого підходу? Яким є рівень задоволеності здобувачів вищої освіти "
        "методами навчання і викладання відповідно до результатів опитувань?",
        max_length=1500,
    )

    # Paragraph 3
    academic_freedom = models.TextField(
        verbose_name="Відповідність методів за принципам академічної свободи",
        help_text="Продемонструйте, яким чином забезпечується відповідність методів навчання і викладання на ОП "
        "принципам академічної свободи",
        max_length=1500,
    )

    # Paragraph 4
    learning_outcomes = models.TextField(
        verbose_name="Строки надання інформації учасникам",
        help_text="Опишіть, яким чином і у які строки учасникам освітнього процесу надається інформація щодо цілей, "
        "змісту та очікуваних результатів навчання, "
        "порядку та критеріїв оцінювання у межах окремих освітніх компонентів",
        max_length=1500,
    )

    # Paragraph 5
    learning_and_research = models.TextField(
        verbose_name="Навчання та дослідження",
        help_text="Опишіть, яким чином відбувається поєднання навчання і досліджень під час реалізації ОП",
        max_length=3000,
    )

    # Paragraph 6
    curriculum_update = models.TextField(
        verbose_name="Оновлення змісту навчальної програми",
        help_text="Продемонструйте, із посиланням на конкретні приклади, "
        "яким чином викладачі оновлюють зміст освітніх компонентів на основі наукових досягнень "
        "і сучасних практик у відповідній галузі",
        max_length=3000,
    )

    # Paragraph 7
    internationalization = models.TextField(
        verbose_name="Інтернаціоналізація діяльності",
        help_text="Опишіть, яким чином навчання, викладання та наукові дослідження у межах ОП "
        "пов’язані із інтернаціоналізацією діяльності ЗВО",
        max_length=1500,
    )

    class Meta:
        db_table = "educational_program_learning_and_teaching"
        verbose_name = "Навчання і викладання за освітньою програмою"
        verbose_name_plural = "Навчання і викладання за освітніх програм"


# 5. Контрольні заходи, оцінювання здобувачів вищої освіти та академічна доброчесність
class ControlMeasuresAndAcademicIntegrity(models.Model):
    # Paragraph 1
    description = models.TextField(
        verbose_name="Опис форм контрольних заходів",
        help_text="Опишіть, яким чином форми контрольних заходів у межах навчальних дисциплін \
                   ОП дозволяють перевірити досягнення програмних результатів навчання?",
        max_length=3000,
    )
    # Paragraph 2
    clarity_criteria = models.TextField(
        verbose_name="Чіткість та зрозумілість форм",
        help_text="Яким чином забезпечуються чіткість та зрозумілість форм контрольних заходів \
                   та критеріїв оцінювання навчальних досягнень здобувачів вищої освіти?",
        max_length=1500,
    )
    # Paragraph 3
    information_provision = models.TextField(
        verbose_name="Надання інформації здобувачам",
        help_text="Яким чином і у які строки інформація про форми контрольних заходів \
                   та критерії оцінювання доводяться до здобувачів вищої освіти?",
        max_length=1500,
    )
    # Paragraph 4
    compliance_requirements = models.TextField(
        verbose_name="Відповідність форм атестації",
        help_text="Яким чином форми атестації здобувачів вищої освіти відповідають \
                   вимогам стандарту вищої освіти (за наявності)?",
        max_length=1500,
    )
    # Paragraph 5
    accessibility_certification_procedure = models.TextField(
        verbose_name="Процедура проведення контрольних заходів",
        help_text="Яким документом ЗВО регулюється процедура проведення контрольних заходів? "
        "Яким чином забезпечується його доступність для учасників освітнього процесу?",
        max_length=1500,
    )
    # Paragraph 6
    objectivity_procedures = models.TextField(
        verbose_name="Процедури врегулювання конфлікту інтересів. "
        "Процедури об'єктивності єкзаменаторів",
        help_text="Яким чином ці процедури забезпечують об’єктивність екзаменаторів? "
        "Якими є процедури запобігання та врегулювання конфлікту інтересів? "
        "Наведіть приклади застосування відповідних процедур на ОП",
        max_length=1500,
    )
    # Paragraph 7
    repeating_control_measures_procedures = models.TextField(
        verbose_name="Процедури врегулювання порядку "
        "повторного проходження контрольних заходів",
        help_text="Яким чином процедури ЗВО урегульовують порядок повторного проходження контрольних заходів? "
        "Наведіть приклади застосування відповідних правил на ОП",
        max_length=1500,
    )
    # Paragraph 8
    appeal_procedure_and_results_of_control_measures = models.TextField(
        verbose_name="Процедури врегулювання порядку "
        "повторного проходження контрольних заходів",
        help_text="Яким чином процедури ЗВО урегульовують порядок оскарження процедури "
        "та результатів проведення контрольних заходів? "
        "Наведіть приклади застосування відповідних правил на ОП",
        max_length=1500,
    )
    # Paragraph 9
    policies_and_standards_documents = models.TextField(
        verbose_name="Документи про політику, стандарти, процедури академічної доброчесності",
        help_text="Які документи ЗВО містять політику, стандарт и і процедури дотримання академічної доброчесності?",
        max_length=1500,
    )
    # Paragraph 10
    combating_violations_of_academic_integrity_solutions = models.TextField(
        verbose_name="Технологічні рішення протидії порушенням академічної доброчесності",
        help_text="Які технологічні рішення використовуються на ОП "
        "як інструменти протидії порушенням академічної доброчесності?",
        max_length=1500,
    )
    # Paragraph 11
    promoting_academic_integrity = models.TextField(
        verbose_name="Популярізація академічної доброчесності",
        help_text="Яким чином ЗВО популяризує академічну доброчесність серед здобувачів вищої освіти ОП?",
        max_length=1500,
    )
    # Paragraph 12
    responding_to_violations_of_academic_integrity = models.TextField(
        verbose_name="Реагування на порушення академічної доброчесності",
        help_text="Яким чином ЗВО реагує на порушення академічної доброчесності? "
        "Наведіть приклади відповідних ситуацій щодо здобувачів вищої освіти відповідної ОП",
        max_length=1500,
    )

    class Meta:
        db_table = "control_measures_and_academic_integrity"
        verbose_name = "Контрольний захід, оцінювання здобувача вищої освіти та академічна доброчесність"
        verbose_name_plural = "Контрольні заходи, оцінювання здобувачів вищої освіти та академічна доброчесність"


# 6. Людські ресурси
class HumanResources(models.Model):
    # 1
    competency_level = models.TextField(
        verbose_name="Рівень професіоналізму",
        help_text="Яким чином під час конкурсного добору викладачів ОП забезпечується "
        "необхідний рівень їх професіоналізму?",
        max_length=1500,
    )
    # 2
    employers_engagement = models.TextField(
        verbose_name="Залучення роботодавців",
        help_text="Опишіть, із посиланням на конкретні приклади, яким чином ЗВО залучає роботодавців до організації "
        "та реалізації освітнього процесу",
        max_length=1500,
    )
    # 3
    expert_involvement = models.TextField(
        verbose_name="Залучення професіоналів-практиків",
        help_text="Опишіть, із посиланням на конкретні приклади, яким чином ЗВО залучає до аудиторних занять "
        "на ОП професіоналів-практиків, експертів галузі, представників роботодавців",
        max_length=1500,
    )
    # 4
    teacher_development = models.TextField(
        verbose_name="Розвиток викладачів ОП",
        help_text="Опишіть, яким чином ЗВО сприяє професійному розвиткові викладачів ОП? "
        "Наведіть конкретні приклади такого сприяння",
        max_length=1500,
    )
    # 5
    teaching_excellence = models.TextField(
        verbose_name="Стимулювання розвитку викладацької майстерності",
        help_text="Продемонструйте, що ЗВО стимулює розвиток викладацької майстерності",
        max_length=1500,
    )

    class Meta:
        db_table = "human_resources"
        verbose_name = "Людський ресурс"
        verbose_name_plural = "Людські ресурси"


# 7. Освітнє середовище та матеріальні ресурси
class EducationalEnvironmentAndMaterialResources(models.Model):
    # 1
    financial_resources = models.TextField(
        verbose_name="Фінансові та матеріально-технічні ресурси",
        help_text="Продемонструйте, яким чином фінансові та матеріально-технічні ресурси "
        "(бібліотека, інша інфраструктура, обладнання тощо), "
        "а також навчально-методичне забезпечення ОП забезпечують досягнення визначених ОП цілей "
        "та програмних результатів навчання?",
        max_length=1500,
    )
    # 2
    educational_environment = models.TextField(
        verbose_name="Освітнє середовище",
        help_text="Продемонструйте, яким чином освітнє середовище, створене у ЗВО, "
        "дозволяє задовольнити потреби та інтереси здобувачів вищої освіти ОП? "
        "Які заходи вживаються ЗВО задля виявлення і врахування цих потреб та інтересів?",
        max_length=1500,
    )
    # 3
    safety_measures = models.TextField(
        verbose_name="Безпека освітнього середовища",
        help_text="Опишіть, яким чином ЗВО забезпечує безпечність освітнього середовища "
        "для життя та здоров’я здобувачів вищої освіти (включаючи психічне здоров’я)",
        max_length=1500,
    )
    # 4
    support_services = models.TextField(
        verbose_name="Підтримка здобувачів вищої освіти",
        help_text="Опишіть механізми освітньої, організаційної, інформаційної, консультативної "
        "та соціальної підтримки здобувачів вищої освіти? "
        "Яким є рівень задоволеності здобувачів вищої освіти цією підтримкою "
        "відповідно до результатів опитувань?",
        max_length=3000,
    )
    # 5
    special_needs_people_education = models.TextField(
        verbose_name="Освіта осіб з особливими потребами",
        help_text="Яким чином ЗВО створює достатні умови для реалізації права на освіту особами "
        "з особливими освітніми потребами? "
        "Наведіть конкретні приклади створення таких умов на ОП (якщо такі були)",
        max_length=1500,
    )
    # 6
    policy_and_procedures_for_conflict_resolution = models.TextField(
        verbose_name="Політика та процедури врегулювання конфліктних ситуацій",
        help_text="Яким чином у ЗВО визначено політику та процедури врегулювання конфліктних ситуацій "
        "(включаючи пов’язаних із сексуальними домаганнями, дискримінацією та корупцією)? "
        "Яким чином забезпечується їх доступність політики та процедур врегулювання "
        "для учасників освітнього процесу? "
        "Якою є практика їх застосування під час реалізації ОП?",
        max_length=3000,
    )

    class Meta:
        db_table = "educational_environment_and_material_resources"
        verbose_name = "Освітнє середовище та матеріальний ресурс"
        verbose_name_plural = "Освітні середовища та матеріальні ресурси"


# 8. Внутрішнє забезпечення якості освітньої програми
class QualityAssurance(models.Model):
    # 1
    regulatory_document = models.TextField(
        max_length=1500,
        verbose_name="Регуляторний документ ОП",
        help_text="Яким документом ЗВО регулюються процедури розроблення, затвердження, моніторингу "
        "та періодичного перегляду ОП? "
        "Наведіть посилання на цей документ, оприлюднений у відкритому доступі в мережі Інтернет. ",
    )
    # 2
    education_program_review = models.TextField(
        max_length=3000,
        verbose_name="Перегляд ОП",
        help_text="Опишіть, яким чином та з якою періодичністю відбувається перегляд ОП? "
        "Які зміни були внесені до ОП за результатами останнього перегляду, чим вони були обґрунтовані?",
    )

    # 2
    involvement_of_students = models.TextField(
        max_length=1500,
        verbose_name="Залучення студентів до процесу періодичного перегляду ОП",
        help_text="Продемонструйте, із посиланням на конкретні приклади, як здобувачі вищої освіти залучені "
        "до процесу періодичного перегляду ОП та інших процедур забезпечення її якості, "
        "а їх позиція береться до уваги під час перегляду ОП",
    )

    # 3
    student_self_government = models.TextField(
        max_length=1500,
        verbose_name="Студентське самоврядування",
        help_text="Яким чином студентське самоврядування бере участь у процедурах внутрішнього забезпечення якості ОП",
    )

    # 4
    involvement_of_employers = models.TextField(
        max_length=1500,
        verbose_name="Залучення роботодавців",
        help_text="Продемонструйте, із посиланням на конкретні приклади, як роботодавці безпосередньо "
        "або через свої об’єднання залучені до процесу періодичного перегляду ОП "
        "та інших процедур забезпечення її якості.",
    )

    # 5
    alumni_employment = models.TextField(
        max_length=1500,
        verbose_name="Траєкторії працевлаштування випускників ОП",
        help_text="Опишіть практику збирання та врахування інформації щодо кар’єрного шляху "
        "та траєкторій працевлаштування випускників ОП.",
    )

    # 6
    quality_issues = models.TextField(
        max_length=3000,
        verbose_name="Недоліки в ОП та реакція на них",
        help_text="Які недоліки в ОП та/або освітній діяльності з реалізації ОП були виявлені "
        "у ході здійснення процедур внутрішнього забезпечення якості за час її реалізації? "
        "Яким чином система забезпечення якості ЗВО відреагувала на ці недоліки?.",
    )

    # 7
    educational_program_improvement = models.TextField(
        max_length=3000,
        verbose_name="Удосконалення ОП",
        help_text="Продемонструйте, що результати зовнішнього забезпечення якості вищої освіти "
        "беруться до уваги під час удосконалення ОП. "
        "Яким чином зауваження та пропозиції з останньої акредитації та акредитацій інших ОП "
        "були ураховані під час удосконалення цієї ОП?.",
    )

    # 8
    academic_community_members_engaging = models.TextField(
        max_length=1500,
        verbose_name="Залучення учасників академічної спільноти",
        help_text="Опишіть, яким чином учасники академічної спільноти змістовно залучені "
        "до процедур внутрішнього забезпечення якості ОП?.",
    )

    # 9
    structural_units_responsibilities_distribution = models.TextField(
        max_length=1500,
        verbose_name="Розподіл відповідальності між різними структурними підрозділами ЗВО",
        help_text="Опишіть розподіл відповідальності між різними структурними підрозділами ЗВО "
        "у контексті здійснення процесів і процедур внутрішнього забезпечення якості освіти.",
    )

    class Meta:
        db_table = "quality_assurance"
        verbose_name = "Внутрішнє забезпечення якості освітньої програми"
        verbose_name_plural = "Внутрішнє забезпечення якості освітніх програм"


# 9. Прозорість і публічність
class EducationalTransparencyAndPublicity(models.Model):
    # 1
    regulatory_documents = models.CharField(
        max_length=1500,
        verbose_name="Регуляторні документи",
        help_text="Документи, що регулюють права та обов'язки усіх учасників освітнього процесу та їх доступність "
        "для учасників освітнього процесу.",
    )
    # 2
    stakeholder_feedback_link = models.URLField(
        verbose_name="Посилання на веб-сторінку для отримання зауважень та пропозицій",
        help_text="Адреса веб-сторінки на офіційному веб-сайті ЗВО, де можна знайти проект з метою отримання зауважень "
        "та пропозицій від заінтересованих сторін (стейкхолдерів).",
    )
    # 3
    educational_program_link = models.URLField(
        verbose_name="Посилання на інформацію про освітню програму",
        help_text="Адреса веб-сторінки, де можна знайти оприлюднену у відкритому доступі в мережі Інтернет "
        "інформацію про освітню програму (включаючи її цілі, очікувані результати навчання та компоненти).",
    )

    class Meta:
        db_table = "educational_transparency_and_publicity"
        verbose_name = "Прозорість та публічність"
        verbose_name_plural = "Прозорість та публічність"


# 10. Навчання через дослідження. (Заповнюється лише для ОП третього (освітньо-наукового) рівня)
class EducationalProgram(models.Model):
    # 1
    description = models.TextField(
        max_length=1500,
        verbose_name="Відповідність ОП науковим інтересам аспірантів",
        help_text="Продемонструйте, що зміст освітньо-наукової програми "
        "відповідає науковим інтересам аспірантів (ад’юнктів)",
    )
    # 2
    research_preparation = models.TextField(
        max_length=3000,
        verbose_name="Підготовка до дослідницької діяльності",
        help_text="Опишіть, яким чином зміст освітньо-наукової програми забезпечує повноцінну підготовку "
        "здобувачів вищої освіти до дослідницької діяльності за спеціальністю та/або галуззю",
    )
    # 3
    teaching_preparation = models.TextField(
        max_length=3000,
        verbose_name="Підготовка до викладацької діяльності у ЗВО",
        help_text="Опишіть, яким чином зміст освітньо-наукової програми забезпечує повноцінну підготовку "
        "здобувачів вищої освіти до викладацької діяльності у закладах вищої освіти "
        "за спеціальністю та/або галуззю",
    )
    # 4
    supervisor_relevance = models.TextField(
        max_length=1500,
        verbose_name="Дотичність тем наукових досліджень аспірантів та керівників",
        help_text="Продемонструйте дотичність тем наукових досліджень аспірантів (ад’юнктів) "
        "напрямам досліджень наукових керівників",
    )
    # 5
    research_support = models.TextField(
        max_length=1500,
        verbose_name="Можливості для проведення і апробації наукових досліджень",
        help_text="Опишіть з посиланням на конкретні приклади, як ЗВО організаційно та матеріально забезпечує "
        "в межах освітньо-наукової програми можливості для проведення і апробації результатів "
        "наукових досліджень аспірантів (ад’юнктів)",
    )
    # 6
    international_participation = models.TextField(
        max_length=1500,
        verbose_name="Долучення аспірантів до міжнародної академічної спільноти",
        help_text="Проаналізуйте, як ЗВО забезпечує можливості для долучення аспірантів (ад’юнктів) "
        "до міжнародної академічної спільноти за спеціальністю, наведіть конкретні проекти та заходи",
    )
    # 7
    research_projects_supervisors_participation = models.TextField(
        max_length=1500,
        verbose_name="Участь наукових керівників у дослідницьких проектах",
        help_text="Опишіть участь наукових керівників аспірантів у дослідницьких проектах, "
        "результати яких регулярно публікуються та/або практично впроваджуються",
    )
    # 8
    academic_integrity_practices = models.TextField(
        max_length=1500,
        verbose_name="Практики дотримання академічної доброчесності",
        help_text="Опишіть чинні практики дотримання академічної доброчесності у науковій діяльності "
        "наукових керівників та аспірантів (ад’юнктів)",
    )
    # 9
    academic_integrity_preventing_violations = models.TextField(
        max_length=1500,
        verbose_name="Запобігання порушенню академічної доброчесності",
        help_text="Продемонструйте, що ЗВО вживає заходів для виключення можливості здійснення наукового керівництва "
        "особами, які вчинили порушення академічної доброчесності",
    )

    class Meta:
        db_table = "educational_program"
        verbose_name = "Прозорість та публічність"
        verbose_name_plural = "Прозорість та публічність"


# 11. Перспективи подальшого розвитку ОП
class EducationalProgramDevelopmentPerspectives(models.Model):
    # 1
    strong_weak_points = models.TextField(
        max_length=3000,
        verbose_name="Сильні та слабкі сторони ОП",
        help_text="Опис загальних сильних та слабких сторін ОП",
    )
    # 2
    future_development = models.TextField(
        max_length=1500,
        verbose_name="Перспективи розвитку ОП на найближчі 3 роки",
        help_text="Опис конкретних заходів, які ЗВО планує здійснити для реалізації перспектив розвитку ОП",
    )

    class Meta:
        db_table = "op_development_perspectives"
        verbose_name = "Перспектива подальшого розвитку ОП"
        verbose_name_plural = "Перспективи подальшого розвитку ОП"

    def __str__(self):
        return f"{self.id}"


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
        "Teacher",
        verbose_name="ПІБ викладача",
        help_text="Повне ім'я викладача",
        on_delete=models.PROTECT,
    )
    # 3
    # TODO: check Foreign Key
    structural_subdivision = models.ForeignKey(
        "StructuralSubdivision",
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
        db_table = "table_annex"
        verbose_name = "Загальна відомость"
        verbose_name_plural = "Загальні відомості"


# Загальні відповіді на питання
class GeneralQuestionAnswer(models.Model):
    educational_program_design = models.ForeignKey(
        "EducationalProgramDesign",
        on_delete=models.PROTECT,
        verbose_name="Проектування та цілі освітньої програми",
    )
    educational_program_structure_and_content = models.ForeignKey(
        "EducationalProgramStructureAndContent",
        on_delete=models.PROTECT,
        verbose_name="Структура та зміст освітньої програми",
    )
    educational_program_access = models.ForeignKey(
        "EducationalProgramAccess",
        on_delete=models.PROTECT,
        verbose_name="Доступ до освітньої програми та визнання результатів навчання",
    )
    educational_program_learning_and_teaching = models.ForeignKey(
        "EducationalProgramLearningAndTeaching",
        on_delete=models.PROTECT,
        verbose_name="Навчання і викладання за освітньою програмою",
    )
    control_measures_and_academic_integrity = models.ForeignKey(
        "ControlMeasuresAndAcademicIntegrity",
        on_delete=models.PROTECT,
        verbose_name="Контрольні заходи, оцінювання здобувачів вищої освіти та академічна доброчесність",
    )
    human_resources = models.ForeignKey(
        "HumanResources", on_delete=models.PROTECT, verbose_name="Людські ресурси"
    )
    educational_environment_and_material_resources = models.ForeignKey(
        "EducationalEnvironmentAndMaterialResources",
        on_delete=models.PROTECT,
        verbose_name="Освітнє середовище та матеріальні ресурси",
    )
    quality_assurance = models.ForeignKey(
        "QualityAssurance",
        on_delete=models.PROTECT,
        verbose_name="Внутрішнє забезпечення якості освітньої програми",
    )
    educational_transparency_and_publicity = models.ForeignKey(
        "EducationalTransparencyAndPublicity",
        on_delete=models.PROTECT,
        verbose_name="Прозорість і публічність",
    )
    educational_program = models.ForeignKey(
        "EducationalProgram",
        on_delete=models.PROTECT,
        verbose_name="EducationalProgram",
    )
    educational_program_development_perspectives = models.ForeignKey(
        "EducationalProgramDevelopmentPerspectives",
        on_delete=models.PROTECT,
        verbose_name="Перспективи подальшого розвитку ОП",
    )

    class Meta:
        db_table = "table_annex"
        verbose_name = "Додаток до довідника про самооцінювання ОП(таблиці)"
        verbose_name_plural = "Додатки до довідника про самооцінювання ОП(таблиці)"


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


# Фінальна таблиця що зберігає всб інформацію по ВІДОМОСТІ ПРО САМООЦІНЮВАННЯ ОСВІТНЬОЇ ПРОГРАМИ
class InformationOnSelfAssessmentOfEducationalProgram(models.Model):
    # Part 1
    general_information = models.ForeignKey(
        "GeneralInformation",
        on_delete=models.PROTECT,
        related_name="general_information_self_assessment",
        verbose_name="Загальні відомості",
        help_text="Перша частина довідника, що містить інформацію про ЗВО та ОП",
    )
    # Part 2
    general_question_answer = models.ForeignKey(
        "GeneralQuestionAnswer",
        on_delete=models.PROTECT,
        related_name="general_question_answer_self_assessment",
        verbose_name="Відповіді на загальні питання",
        help_text="Друга частина довідника, що містить відповіді на загальні питання",
    )
    # Tables
    tables_annex = models.ForeignKey(
        "TablesAnnex",
        on_delete=models.PROTECT,
        related_name="tables_annex_self_assessment",
        verbose_name="Таблиці додаток",
        help_text="Додаток до довідника про самооцінювання ОП(таблиці)",
    )

    class Meta:
        db_table = "information_on_self_assessment_of_educational_program"
        verbose_name = "Довідник про самооцінювання ОП"
        verbose_name_plural = "Довідники про самооцінювання ОП"
