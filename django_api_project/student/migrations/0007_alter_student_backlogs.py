# Generated by Django 5.1.6 on 2025-02-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='backlogs',
            field=models.CharField(max_length=10),
        ),
    ]
