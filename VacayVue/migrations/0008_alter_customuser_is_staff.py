# Generated by Django 5.0.3 on 2024-03-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VacayVue', '0007_customuser_permissions_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
