# Generated by Django 2.1.4 on 2019-01-04 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_option', '0002_auto_20190104_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appoption',
            old_name='socal',
            new_name='social',
        ),
    ]