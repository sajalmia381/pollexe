# Generated by Django 2.1.4 on 2018-12-31 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181231_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='images',
            new_name='image',
        ),
    ]
