# Generated by Django 4.0.5 on 2022-06-20 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('table_type', models.CharField(default='', max_length=20)),
                ('inverter_type', models.CharField(default='', max_length=20)),
                ('module_type', models.CharField(default='', max_length=20)),
                ('plant_size', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('plant_capacity', models.CharField(default='', max_length=20)),
                ('project_created_date', models.DateField()),
                ('center', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('properties', models.TextField(default='{}')),
                ('project_dates', models.TextField(default='{}')),
                ('status', models.CharField(choices=[('created', 'created'), ('ftp', 'ftp'), ('processing', 'processing'), ('completed', 'completed')], default='created', max_length=50)),
                ('clients', models.ManyToManyField(related_name='client', to='auth.group')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.userprofile')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org', to='auth.group')),
                ('shared_profile', models.ManyToManyField(related_name='shared_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProcessedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ortho_file_location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('kml_file_location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('cad_file_location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('thermal_hotspot_location', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('summary_layers', models.TextField(blank=True, default='{}', null=True)),
                ('inverter_layers', models.TextField(blank=True, default='{}', null=True)),
                ('topography_layers', models.TextField(blank=True, default='{}', null=True)),
                ('power_loss', models.TextField(blank=True, default='{}', null=True)),
                ('properties', models.TextField(default='{}')),
                ('total_modules_present', models.CharField(default='0', max_length=20)),
                ('plant_size_scanned', models.CharField(default='0', max_length=20)),
                ('total_power_loss', models.CharField(default='0', max_length=20)),
                ('total_defects', models.CharField(default='0', max_length=20)),
                ('report_path', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('status', models.CharField(choices=[('created', 'created'), ('ftp', 'ftp'), ('processing', 'processing'), ('completed', 'completed')], default='created', max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_module.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', models.TextField(default='{}')),
                ('environmental_condition', models.TextField(blank=True, default='{}', null=True)),
                ('payload_check', models.TextField(blank=True, default='{}', null=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_module.projectprocesseddata')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_module.project')),
            ],
        ),
    ]
