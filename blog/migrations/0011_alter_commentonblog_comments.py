# Generated by Django 3.2.2 on 2021-05-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210525_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentonblog',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
