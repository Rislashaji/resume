# Generated by Django 4.2.5 on 2023-10-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapi', '0007_rename_resume_id_tb_resume_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_skill',
            name='resume_id',
        ),
        migrations.RemoveField(
            model_name='tb_skill',
            name='user_id',
        ),
    ]
