# Generated by Django 5.0.1 on 2024-01-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_categorymodel_options_categorymodel_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='thumnail',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='تصویر'),
        ),
    ]
