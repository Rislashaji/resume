# Generated by Django 4.2.5 on 2023-10-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapi', '0010_tb_register_dob_tb_register_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_register',
            name='status',
            field=models.CharField(default='applied', max_length=100),
        ),
    ]
