# Generated by Django 4.2.5 on 2023-10-06 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumedetector', '0014_tb_details_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_job_application',
            name='cmpny_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resumedetector.tb_cmpny_register'),
        ),
    ]
