# Generated by Django 4.0.10 on 2024-10-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_alter_qualification_date_awarded"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="graduation_year",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Рік закінчення"
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="specialty",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Спеціальність"
            ),
        ),
        migrations.AlterField(
            model_name="professionaldevelopment",
            name="duration",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Тривалість"
            ),
        ),
        migrations.AlterField(
            model_name="professionaldevelopment",
            name="type",
            field=models.CharField(
                blank=True,
                max_length=600,
                null=True,
                verbose_name="Тип (сертифікат, свідоцтво)",
            ),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="date_awarded",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Дата присудження або код спеціальності",
            ),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="details",
            field=models.TextField(blank=True, null=True, verbose_name="Деталі"),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="dissertation_topic",
            field=models.TextField(
                blank=True, null=True, verbose_name="Тема дисертації"
            ),
        ),
    ]
