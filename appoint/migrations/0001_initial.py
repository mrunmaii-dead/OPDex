# Generated by Django 5.0.6 on 2024-06-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('doctor', models.CharField(choices=[('OPD', 'Opd'), ('ENT', 'Ent')], max_length=100)),
                ('complaint', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reg_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(default=0)),
                ('email', models.EmailField(default='youremail@gmail.com', max_length=254)),
                ('age', models.IntegerField(default=0)),
                ('blood_group', models.CharField(default='A+', max_length=3)),
                ('gender', models.CharField(default='M', max_length=3)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.CharField(default='100', max_length=5)),
                ('recognition_mark', models.CharField(default='NA', max_length=200)),
                ('allergen', models.CharField(default='NA', max_length=200)),
            ],
        ),
    ]