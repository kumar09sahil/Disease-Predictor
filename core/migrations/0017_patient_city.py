# Generated by Django 5.0.1 on 2024-03-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_patient_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]