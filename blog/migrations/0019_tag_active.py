# Generated by Django 2.1.4 on 2019-01-17 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_comment_timestimp'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]