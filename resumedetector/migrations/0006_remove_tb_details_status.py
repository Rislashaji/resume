# Generated by Django 4.2.5 on 2023-10-05 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumedetector', '0005_tb_details_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_details',
            name='status',
        ),
    ]
