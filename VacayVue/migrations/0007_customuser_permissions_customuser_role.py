# Generated by Django 5.0.3 on 2024-03-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VacayVue', '0006_remove_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='permissions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
