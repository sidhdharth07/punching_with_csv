# Generated by Django 4.2.4 on 2023-08-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thisapp', '0003_alter_registermodel_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing_model',
            name='durations',
            field=models.CharField(null=True),
        ),
    ]
