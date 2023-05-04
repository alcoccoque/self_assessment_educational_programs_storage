# Generated by Django 4.0.10 on 2023-05-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_information', '0003_alter_educationprogramaccreditationinformation_field_of_study_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationstatistics',
            name='study_course_year',
            field=models.IntegerField(choices=[('1', '1 рік навчання'), ('2', '2 рік навчання'), ('3', '3 рік навчання'), ('4', '4 рік навчання')], help_text='Рік навчання', verbose_name='Рік навчання'),
        ),
    ]
