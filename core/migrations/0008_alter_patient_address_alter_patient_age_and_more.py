# Generated by Django 5.0.1 on 2024-03-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_patient_gender_alter_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(default='', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_pressure',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.FloatField(default=0, null=True),
        ),
    ]