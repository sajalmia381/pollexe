# Generated by Django 2.1.4 on 2019-01-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_tag_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag_list',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Tag'),
        ),
    ]