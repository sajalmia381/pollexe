# Generated by Django 2.1.4 on 2019-01-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('logo_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
