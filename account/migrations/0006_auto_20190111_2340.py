# Generated by Django 2.1.4 on 2019-01-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, help_text="Leave This it' will create instance of email", max_length=30),
        ),
    ]