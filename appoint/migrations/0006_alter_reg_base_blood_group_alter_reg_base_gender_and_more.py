# Generated by Django 5.0.6 on 2024-06-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0005_alter_reg_base_email_alter_reg_base_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_base',
            name='blood_group',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='reg_base',
            name='gender',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='reg_base',
            name='height',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]