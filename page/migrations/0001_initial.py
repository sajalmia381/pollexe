# Generated by Django 2.1.4 on 2018-12-30 05:34

from django.db import migrations, models
import django.utils.timezone
import page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=page.models.here_image_name_generator)),
                ('timestimp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
