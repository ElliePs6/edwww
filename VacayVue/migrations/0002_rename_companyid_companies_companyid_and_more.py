# Generated by Django 5.0.3 on 2024-03-24 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VacayVue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='CompanyID',
            new_name='companyID',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmployID',
            new_name='employeeID',
        ),
        migrations.RemoveField(
            model_name='companies',
            name='Companyname',
        ),
        migrations.RemoveField(
            model_name='companies',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='CompanyID',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Firstname',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Lastname',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Role',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='Username',
        ),
        migrations.AddField(
            model_name='companies',
            name='hrname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='companies_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='VacayVue.companies'),
        ),
        migrations.AddField(
            model_name='employees',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_profiles', to='VacayVue.companies'),
        ),
        migrations.AddField(
            model_name='employees',
            name='join_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requests',
            name='EmployID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='VacayVue.employees'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='EndDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='StartDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='companyname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='username',
            field=models.CharField(max_length=225, null=True),
        ),
    ]