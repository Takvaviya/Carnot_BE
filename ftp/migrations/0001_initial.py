# Generated by Django 4.0.5 on 2022-07-11 07:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_module', '0002_alter_project_id_alter_projectdata_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploaderLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_by', models.CharField(blank=True, max_length=50, null=True)),
                ('allfiles', models.TextField(default='')),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_number_of_files', models.IntegerField(default=0)),
                ('number_of_files_uploaded', models.IntegerField(default=0)),
                ('filesuploaded', models.TextField(default='')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_module.projectdata')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_module.project')),
            ],
        ),
    ]
