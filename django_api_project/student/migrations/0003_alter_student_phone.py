# Generated by Django 5.1.6 on 2025-02-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_phone_alter_student_rno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
