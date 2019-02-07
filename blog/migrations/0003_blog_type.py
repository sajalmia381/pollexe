# Generated by Django 2.1.4 on 2018-12-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.CharField(blank=True, choices=[('collection', 'Collection'), ('review', 'Review')], default='collection', max_length=20, null=True),
        ),
    ]