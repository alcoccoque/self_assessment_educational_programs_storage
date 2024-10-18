# Generated by Django 4.0.10 on 2023-05-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("general_question_answer", "0001_initial"),
        ("general_information", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationprogramaccreditationinformation",
            name="field_of_study",
            field=models.ForeignKey(
                help_text="Галузь знань",
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.fieldofstudy",
                verbose_name="Галузь знань",
            ),
        ),
        migrations.AlterField(
            model_name="educationprogramaccreditationinformation",
            name="grants_professional_qualification",
            field=models.IntegerField(
                choices=[(None, "(Невідомо)"), (0, "Ні"), (1, "Так")],
                help_text="Освітня програма передбачає присвоєння професійної кваліфікації",
                verbose_name="Присвоєння професійної кваліфікації ОП",
            ),
        ),
        migrations.RemoveField(
            model_name="educationprogramaccreditationinformation",
            name="language_of_instruction",
        ),
        migrations.AddField(
            model_name="educationprogramaccreditationinformation",
            name="language_of_instruction",
            field=models.ManyToManyField(
                help_text="Мова (мови) викладання",
                to="general_question_answer.language",
                verbose_name="Мова викладання",
            ),
        ),
        migrations.AlterField(
            model_name="educationprogramaccreditationinformation",
            name="specialty",
            field=models.ForeignKey(
                help_text="Спеціальність",
                on_delete=django.db.models.deletion.PROTECT,
                to="general_information.specialty",
                verbose_name="Спеціальність",
            ),
        ),
    ]
