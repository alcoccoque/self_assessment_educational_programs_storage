# Generated by Django 4.0.10 on 2023-05-04 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0002_teacher_student"),
        ("general_information", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="separatestructuralunit",
            name="head_full_name",
            field=models.ForeignKey(
                help_text="ПІБ керівника ВСП ЗВО",
                on_delete=django.db.models.deletion.PROTECT,
                to="users.teacher",
                verbose_name="ПІБ керівника",
            ),
        ),
        migrations.AddField(
            model_name="otherhighereducationprogram",
            name="education_program",
            field=models.ManyToManyField(
                related_name="other_higher_education_program",
                to="general_information.educationprogram",
            ),
        ),
        migrations.AddField(
            model_name="highereducationinstitutioninformation",
            name="hei",
            field=models.ForeignKey(
                help_text="Інформація про заклад вищої освіти",
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.highereducationinstitution",
                verbose_name="Заклад вищої освіти",
            ),
        ),
        migrations.AddField(
            model_name="highereducationinstitutioninformation",
            name="ssu",
            field=models.ForeignKey(
                blank=True,
                help_text="Інформація про відокремлений структурний підрозділ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.separatestructuralunit",
                verbose_name="Відокремлений структурний підрозділ",
            ),
        ),
        migrations.AddField(
            model_name="highereducationinstitution",
            name="head_full_name",
            field=models.ForeignKey(
                help_text="ПІБ керівника ЗВО",
                on_delete=django.db.models.deletion.PROTECT,
                to="users.teacher",
                verbose_name="ПІБ керівника",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="education_program_accreditation_information",
            field=models.ForeignKey(
                help_text="Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="education_program_general_information",
                to="general_information.educationprogramaccreditationinformation",
                verbose_name="Загальна інформація про освітню програму, яка подається на акредитацію",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="education_program_document",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.educationprogramdocument",
                verbose_name="Поля для завантаження документів щодо ОП",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="education_program_general_information",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.educationprogramgeneralinformation",
                verbose_name="Загальні відомості про ОП",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="education_statistics",
            field=models.ForeignKey(
                help_text="Інформація про контингент здобувачів вищої освіти на ОП станом на 1 жовтня поточного НР та набір на ОП",
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.educationstatistics",
                verbose_name="Інформація про контингент здобувачів вищої освіти",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="hei_links_in_edebo",
            field=models.ForeignKey(
                help_text="Посилання на інформацію про ЗВО (ВСП ЗВО) у Реєстрі суб’єктів освітньої діяльності ЄДЕБО",
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.heilinksinedebo",
                verbose_name="Посилання на інформацію про ЗВО у Реєстрі ЄДЕБО",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="higher_education_institution_area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.highereducationinstitutionarea",
                verbose_name="Інформація про площі ЗВО, станом на момент подання відомостей про самооцінювання",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="higher_education_institution_information",
            field=models.ForeignKey(
                help_text="Інформація про заклад вищої освіти",
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.highereducationinstitutioninformation",
                verbose_name="Заклад вищої освіти",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="other_higher_education_program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.otherhighereducationprogram",
                verbose_name="Інформація про інші освітні програми ЗВО за відповідною спеціальністю",
            ),
        ),
        migrations.AddField(
            model_name="generalinformation",
            name="self_assessment_educational_program_restricted_info",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.selfassessmenteducationalprogramrestrictedinfo",
                verbose_name="Інформація про наявність в акредитаційній справі інформації з обмеженим доступом",
            ),
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="education_program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="education_program_accreditation_information",
                to="general_information.educationprogram",
            ),
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="field_of_study",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.fieldofstudy",
            ),
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="guarantee_full_name",
            field=models.ForeignKey(
                help_text="ПІБ гаранта ОП",
                on_delete=django.db.models.deletion.PROTECT,
                to="users.teacher",
                verbose_name="ПІБ гаранта",
            ),
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="other_educational_structural_subdivisions",
            field=models.ManyToManyField(
                help_text="Інші навчальні структурні підрозділи (кафедра або інші підрозділи), залучені до реалізації ОП",
                related_name="other_structural_subdivision_ep_accreditation",
                to="general_information.structuralsubdivision",
                verbose_name="Інші навчальні структурні підрозділи",
            ),
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="specialty",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.specialty",
            ),
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="structural_subdivision",
            field=models.ForeignKey(
                help_text="Структурний підрозділ (кафедра або інший підрозділ), відповідальний за реалізацію ОП",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="structural_subdivision_ep_accreditation",
                to="general_information.structuralsubdivision",
                verbose_name="Структурний підрозділ відповідальний за реалізацію ОП",
            ),
        ),
    ]
