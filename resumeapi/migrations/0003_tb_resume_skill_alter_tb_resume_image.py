# Generated by Django 4.2.5 on 2023-09-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapi', '0002_tb_resume_remove_tb_register_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_resume',
            name='skill',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tb_resume',
            name='image',
            field=models.ImageField(default='null.jpeg', upload_to='resume'),
        ),
    ]
