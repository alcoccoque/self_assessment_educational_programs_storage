# Generated by Django 4.0.10 on 2024-10-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_alter_teacher_options_remove_teacher_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professionalactivity",
            name="paragraph",
            field=models.CharField(blank=True, max_length=800, verbose_name="Параграф"),
        ),
        migrations.AlterField(
            model_name="professionaldevelopment",
            name="type",
            field=models.CharField(
                max_length=600, verbose_name="Тип (сертифікат, свідоцтво)"
            ),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="qualification_name",
            field=models.CharField(max_length=600, verbose_name="Назва кваліфікації"),
        ),
        migrations.AlterField(
            model_name="subject",
            name="name",
            field=models.CharField(max_length=600, verbose_name="Навчальна дисципліна"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="position",
            field=models.CharField(blank=True, max_length=600, verbose_name="Посада"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="qualification",
            field=models.CharField(
                blank=True, max_length=600, verbose_name="Кваліфікація викладача"
            ),
        ),
    ]