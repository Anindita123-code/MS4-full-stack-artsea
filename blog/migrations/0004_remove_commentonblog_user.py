# Generated by Django 3.2.2 on 2021-05-24 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_blog_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentonblog',
            name='user',
        ),
    ]
