# Generated by Django 4.2.5 on 2023-10-05 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumedetector', '0010_alter_tb_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_details',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resumedetector.tb_register'),
        ),
    ]
