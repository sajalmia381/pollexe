# Generated by Django 2.1.4 on 2019-01-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('pending', 'Pending'), ('created', 'Created')], default='pending', max_length=25),
        ),
    ]
