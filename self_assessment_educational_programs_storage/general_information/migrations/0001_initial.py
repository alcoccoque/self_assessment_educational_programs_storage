# Generated by Django 4.0.10 on 2023-05-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EducationProgram",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "education_program_id",
                    models.BigIntegerField(
                        help_text="ID освітньої програми в ЄДЕБО",
                        verbose_name="ID освітньої програми",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Назва ОП", max_length=250, verbose_name="Назва ОП"
                    ),
                ),
            ],
            options={
                "verbose_name": "Освітня програма",
                "verbose_name_plural": "Освітні програми",
                "db_table": "education_program",
            },
        ),
        migrations.CreateModel(
            name="EducationProgramAccreditationInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specialty_licensing_info",
                    models.CharField(
                        help_text="Реквізити рішення про ліцензування спеціальності на відповідному рівні вищої освіти",
                        max_length=250,
                        verbose_name="Реквізити рішення про ліцензування спеціальності",
                    ),
                ),
                (
                    "cycle",
                    models.CharField(
                        help_text="Цикл (рівень вищої освіти)",
                        max_length=250,
                        verbose_name="Цикл",
                    ),
                ),
                (
                    "specialization",
                    models.CharField(
                        blank=True,
                        help_text="Спеціалізація",
                        max_length=250,
                        null=True,
                        verbose_name="Спеціалізація",
                    ),
                ),
                (
                    "program_type",
                    models.CharField(
                        help_text="Вид освітньої програми",
                        max_length=250,
                        verbose_name="Вид освітньої програми",
                    ),
                ),
                (
                    "admission_degree",
                    models.CharField(
                        help_text="Вступ на освітню програму здійснюється на основі ступеня (рівня)",
                        max_length=250,
                        verbose_name="Основний ступень",
                    ),
                ),
                (
                    "duration",
                    models.CharField(
                        help_text="Термін навчання на освітній програмі",
                        max_length=255,
                        verbose_name="Термін навчання",
                    ),
                ),
                (
                    "education_program_forms",
                    models.CharField(
                        help_text="Форми здобуття освіти на ОП",
                        max_length=255,
                        verbose_name="Форми здобуття освіти",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        help_text="Місце (адреса) провадження освітньої діяльності за ОП",
                        max_length=255,
                        verbose_name="Місце провадження освітньої діяльності",
                    ),
                ),
                (
                    "grants_professional_qualification",
                    models.CharField(
                        choices=[(None, "(Невідомо)"), (0, "Ні"), (1, "Так")],
                        help_text="Освітня програма передбачає присвоєння професійної кваліфікації",
                        max_length=10,
                        verbose_name="Присвоєння професійної кваліфікації ОП",
                    ),
                ),
                (
                    "professional_qualification",
                    models.CharField(
                        blank=True,
                        help_text="Професійна кваліфікація, яка присвоюється за ОП (за наявності)",
                        max_length=255,
                        null=True,
                        verbose_name="Професійна кваліфікація",
                    ),
                ),
                (
                    "language_of_instruction",
                    models.CharField(
                        help_text="Мова (мови) викладання",
                        max_length=255,
                        verbose_name="Мова викладання",
                    ),
                ),
                (
                    "guarantee_id",
                    models.BigIntegerField(
                        help_text="ID гаранта ОП у ЄДЕБО",
                        verbose_name="ID гаранта у ЄДЕБО",
                    ),
                ),
                (
                    "guarantee_position",
                    models.CharField(
                        help_text="Посада гаранта ОП",
                        max_length=255,
                        verbose_name="Посада гаранта",
                    ),
                ),
                (
                    "guarantee_email",
                    models.EmailField(
                        help_text="Корпоративна електронна адреса гаранта ОП",
                        max_length=254,
                        verbose_name="Корпоративна електронна адреса гаранта",
                    ),
                ),
                (
                    "guarantee_phone",
                    models.CharField(
                        help_text="Контактний телефон гаранта ОП",
                        max_length=20,
                        verbose_name="Контактний телефон гаранта",
                    ),
                ),
                (
                    "additional_phone",
                    models.CharField(
                        blank=True,
                        help_text="Додатковий контактний телефон гаранта ОП",
                        max_length=20,
                        null=True,
                        verbose_name="Додатковий контактний телефон гаранта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Загальна інформація про освітню програму, яка подається на акредитацію",
                "verbose_name_plural": "Загальна інформація про освітні програми, які подаються на акредитацію",
                "db_table": "education_program_accreditation_information",
            },
        ),
        migrations.CreateModel(
            name="EducationProgramDocument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "education_program_doc",
                    models.FileField(
                        help_text="Освітня програма",
                        upload_to="education_program/education_program/",
                        verbose_name="Освітня програма",
                    ),
                ),
                (
                    "curriculum_doc",
                    models.FileField(
                        help_text="Навчальний план за ОП",
                        upload_to="education_program/curriculum/",
                        verbose_name="Навчальний план",
                    ),
                ),
                (
                    "reviews",
                    models.FileField(
                        blank=True,
                        help_text="Рецензії та відгуки роботодавців",
                        null=True,
                        upload_to="education_program/reviews/",
                        verbose_name="Рецензії, відгуки роботодавців",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Поля для завантаження документів щодо ОП",
                "db_table": "education_program_document",
            },
        ),
        migrations.CreateModel(
            name="EducationProgramGeneralInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "history_and_development",
                    models.TextField(
                        help_text="Загальні відомості про ОП, історію її розроблення та впровадження",
                        max_length=3000,
                        verbose_name="Загальні відомості про ОП",
                    ),
                ),
            ],
            options={
                "verbose_name": "Загальні відомості про освітню програму(ОП), історію її розроблення та впровадження",
                "verbose_name_plural": "Загальні відомості про освітні програми(ОП), історію їх розроблення та впровадження",
                "db_table": "education_program_general_information",
            },
        ),
        migrations.CreateModel(
            name="EducationStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "study_course_year",
                    models.PositiveSmallIntegerField(
                        choices=[
                            ("1", "1 рік навчання"),
                            ("2", "2 рік навчання"),
                            ("3", "3 рік навчання"),
                            ("4", "4 рік навчання"),
                        ],
                        help_text="Рік навчання",
                        verbose_name="Рік навчання",
                    ),
                ),
                (
                    "academic_year",
                    models.CharField(
                        help_text="Навчальний рік, у якому відбувся набір здобувачів відповідного року навчання",
                        max_length=11,
                        verbose_name="Навчальний рік",
                    ),
                ),
                (
                    "enrollment",
                    models.PositiveIntegerField(
                        help_text="Обсяг набору на ОП", verbose_name="Обсяг набору"
                    ),
                ),
                (
                    "full_time",
                    models.PositiveIntegerField(
                        help_text="Очна форма навчання", verbose_name="Очна форма"
                    ),
                ),
                (
                    "part_time",
                    models.PositiveIntegerField(
                        help_text="Заочна форма навчання", verbose_name="Заочна форма"
                    ),
                ),
                (
                    "foreign_full_time",
                    models.PositiveIntegerField(
                        help_text="Іноземці, очна форма навчання",
                        verbose_name="Іноземці, очна форма",
                    ),
                ),
                (
                    "foreign_part_time",
                    models.PositiveIntegerField(
                        help_text="Іноземці, заочна форма навчання",
                        verbose_name="Іноземці, заочна форма",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Інформація про контингент здобувачів вищої освіти на ОП станом на 1 жовтня поточного навчального року та набір на ОП",
                "db_table": "education_statistics",
            },
        ),
        migrations.CreateModel(
            name="FieldOfStudy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "field_of_study_code",
                    models.IntegerField(
                        help_text="Код галузі знань", verbose_name="Код галузі знань"
                    ),
                ),
                (
                    "field_of_study",
                    models.CharField(
                        help_text="Галузь знань",
                        max_length=250,
                        verbose_name="Галузь знань",
                    ),
                ),
            ],
            options={
                "verbose_name": "Галузь знань",
                "verbose_name_plural": "Галузі знань",
                "db_table": "field_of_study",
            },
        ),
        migrations.CreateModel(
            name="GeneralInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Загальна відомость",
                "verbose_name_plural": "Загальні відомості",
                "db_table": "general_information",
            },
        ),
        migrations.CreateModel(
            name="HEILinksInEDEBO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        help_text="Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
                        verbose_name="Посилання на інформацію про ЗВО у Реєстрі ЄДЕБО",
                    ),
                ),
            ],
            options={
                "verbose_name": "Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
                "verbose_name_plural": "Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
                "db_table": "hei_links_in_edebo",
            },
        ),
        migrations.CreateModel(
            name="HigherEducationInstitution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hei_id",
                    models.BigIntegerField(
                        help_text="Реєстраційний номер ЗВО у ЄДЕБО",
                        verbose_name="Реєстраційний номер у ЄДЕБО",
                    ),
                ),
                (
                    "higher_educational_institution_name",
                    models.CharField(
                        help_text="Повна назва ЗВО",
                        max_length=250,
                        verbose_name="Повна назва",
                    ),
                ),
                (
                    "institution_code",
                    models.BigIntegerField(
                        help_text="Ідентифікаційний код ЗВО",
                        verbose_name="Ідентифікаційний код",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        help_text="Посилання на офіційний вебсайт ЗВО",
                        verbose_name="Посилання на офіційний вебсайт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Загальна відомість про заклад вищої освіти",
                "verbose_name_plural": "Загальні відомості про заклад вищої освіти",
                "db_table": "higher_educational_institution",
            },
        ),
        migrations.CreateModel(
            name="HigherEducationInstitutionArea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "area_type",
                    models.CharField(
                        choices=[("GA", "Загальна площа"), ("EA", "Навчальна площа")],
                        max_length=2,
                        verbose_name="Тип площі",
                    ),
                ),
                (
                    "all_rooms",
                    models.BigIntegerField(
                        help_text="Усі приміщення ЗВО", verbose_name="Усі приміщення"
                    ),
                ),
                (
                    "own_rooms",
                    models.BigIntegerField(
                        help_text="Власні приміщення ЗВО (на праві власності, господарського відання або оперативного управління)",
                        verbose_name="Власні приміщення",
                    ),
                ),
                (
                    "other_rights_rooms",
                    models.BigIntegerField(
                        help_text="Приміщення, які використовуються на іншому праві, аніж право власності, господарського відання або оперативного управління (оренда, безоплатне користування тощо)",
                        verbose_name="Приміщення з іншим правом власності",
                    ),
                ),
                (
                    "rented_rooms",
                    models.BigIntegerField(
                        help_text="Приміщення, здані в оренду",
                        verbose_name="Приміщення, здані в оренду",
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація про площу ЗВО, станом на момент подання відомостей про самооцінювання, кв. м",
                "verbose_name_plural": "Інформація про площі ЗВО, станом на момент подання відомостей про самооцінювання, кв. м",
                "db_table": "higher_education_institution_area",
            },
        ),
        migrations.CreateModel(
            name="HigherEducationInstitutionInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація про заклад вищої освіти",
                "verbose_name_plural": "Інформація про заклади вищої освіти",
                "db_table": "higher_education_institution_information",
            },
        ),
        migrations.CreateModel(
            name="OtherHigherEducationProgram",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("entry", "Початковий рівень (короткий цикл) вищої освіти"),
                            ("first", "Перший (бакалаврський) рівень"),
                            ("second", "Другий (магістерський) рівень"),
                            (
                                "third",
                                "Третій (освітньонауковий/освітньотворчий) рівень",
                            ),
                        ],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація про іншу освітню програму ЗВО за відповідною спеціальністю",
                "verbose_name_plural": "Інформація про інші освітні програми ЗВО за відповідною спеціальністю",
                "db_table": "other_higher_education_program",
            },
        ),
        migrations.CreateModel(
            name="SelfAssessmentEducationalProgramRestrictedInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "info_description",
                    models.TextField(
                        help_text="Частина відомостей про самооцінювання, яка містить інформацію з обмеженим доступом",
                        verbose_name="Частина відомостей з обмеженим доступом",
                    ),
                ),
                (
                    "info_access_restriction_type",
                    models.TextField(
                        help_text="Вид інформації з обмеженим доступом",
                        verbose_name="Вид інформації з обмеженим доступом",
                    ),
                ),
                (
                    "restricted_info_description",
                    models.TextField(
                        help_text="Опис інформації, доступ до якої обмежений",
                        verbose_name="Опис інформації з обмеженим доступом",
                    ),
                ),
                (
                    "restricting_access_grounds",
                    models.TextField(
                        help_text="Підстава для обмеження доступу до інформації",
                        verbose_name="Підстава для обмеження доступу",
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація про наявність в акредитаційній справі інформації з обмеженим доступом",
                "verbose_name_plural": "Інформація про наявність в акредитаційній справі інформації з обмеженим доступом",
                "db_table": "self_assessment_educational_program_restricted_info",
            },
        ),
        migrations.CreateModel(
            name="SeparateStructuralUnit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ssu_id",
                    models.BigIntegerField(
                        help_text="Реєстраційний номер ВСП ЗВО у ЄДЕБО",
                        verbose_name="Реєстраційний номер ВСП у ЄДЕБО",
                    ),
                ),
                (
                    "separate_structural_unit_name",
                    models.CharField(
                        help_text="Повна назва ВСП ЗВО",
                        max_length=250,
                        verbose_name="Повна назва",
                    ),
                ),
                (
                    "ssu_code",
                    models.BigIntegerField(
                        help_text="Ідентифікаційний код ВСП ЗВО",
                        verbose_name="Ідентифікаційний код",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        help_text="Посилання на офіційний вебсайт ВСП ЗВО",
                        verbose_name="Посилання на офіційний вебсайт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Інформація про відокремлений структурний підрозділ (ВСП)",
                "verbose_name_plural": "Інформація про відокремлений структурний підрозділ (ВСП)",
                "db_table": "separate_structural_unit",
            },
        ),
        migrations.CreateModel(
            name="Specialty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specialty_code",
                    models.IntegerField(
                        help_text="Код спеціальності", verbose_name="Код спеціальності"
                    ),
                ),
                (
                    "specialty",
                    models.CharField(
                        help_text="Спеціальність",
                        max_length=250,
                        verbose_name="Спеціальність",
                    ),
                ),
            ],
            options={
                "verbose_name": "Спеціальність",
                "verbose_name_plural": "Спеціальності",
                "db_table": "specialty",
            },
        ),
        migrations.CreateModel(
            name="StructuralSubdivision",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "responsible_department",
                    models.CharField(
                        help_text="Структурний підрозділ (кафедра або інший підрозділ), відповідальний за реалізацію ОП",
                        max_length=255,
                        verbose_name="Структурний підрозділ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Структурний підрозділ",
                "verbose_name_plural": "Структурні підрозділи",
                "db_table": "structural_subdivision",
            },
        ),
    ]
