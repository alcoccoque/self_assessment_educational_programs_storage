# Generated by Django 4.0.10 on 2024-10-15 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_alter_professionalactivity_paragraph_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                    "institution",
                    models.CharField(
                        max_length=255, verbose_name="Назва навчального закладу"
                    ),
                ),
                (
                    "graduation_year",
                    models.CharField(max_length=10, verbose_name="Рік закінчення"),
                ),
                (
                    "specialty",
                    models.CharField(max_length=255, verbose_name="Спеціальність"),
                ),
                (
                    "qualification_awarded",
                    models.CharField(
                        max_length=255, verbose_name="Отримана кваліфікація"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="teacher",
            name="academic_title",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Вчене звання"
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="faculty",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Факультет"
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="is_main_job",
            field=models.BooleanField(
                default=False, verbose_name="Основне місце роботи"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(max_length=600, verbose_name="Навчальна дисципліна"),
        ),
        migrations.AlterField(
            model_name="professionalactivity",
            name="paragraph",
            field=models.CharField(
                blank=True,
                max_length=800,
                verbose_name="Види і результати професійної діяльності",
            ),
        ),
        migrations.DeleteModel(
            name="Subject",
        ),
        migrations.AddField(
            model_name="education",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="education",
                to="users.teacher",
            ),
        ),
    ]