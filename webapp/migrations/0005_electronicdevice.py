# Generated by Django 4.2.6 on 2023-11-24 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_case_case_saved_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=50)),
                ('make_and_model', models.CharField(max_length=100)),
                ('serial_number_imei', models.CharField(max_length=50, unique=True)),
                ('operating_system', models.CharField(max_length=50)),
                ('storage_capacity', models.CharField(max_length=20)),
                ('connection_ports', models.TextField(blank=True)),
                ('passwords_credentials', models.TextField(blank=True)),
                ('case_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.caseinfo')),
            ],
        ),
    ]
