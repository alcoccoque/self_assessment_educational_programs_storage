# Generated by Django 4.0.10 on 2024-10-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_education_teacher_academic_title_teacher_faculty_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qualification",
            name="date_awarded",
            field=models.CharField(
                blank=True,
                max_length=20,
                verbose_name="Дата присудження або код спеціальності",
            ),
        ),
    ]