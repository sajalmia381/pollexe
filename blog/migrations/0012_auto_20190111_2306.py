# Generated by Django 2.1.4 on 2019-01-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190111_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, help_text='This slug will used for page URL', max_length=250, null=True),
        ),
    ]
