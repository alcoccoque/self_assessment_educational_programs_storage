from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return f"{self.short_name} {self.name}"


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
        db_table = "general_question_answer"
        verbose_name = "Додаток до довідника про самооцінювання ОП(таблиці)"
        verbose_name_plural = "Додатки до довідника про самооцінювання ОП(таблиці)"
