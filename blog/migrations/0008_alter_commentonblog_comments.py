# Generated by Django 3.2.2 on 2021-05-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210524_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentonblog',
            name='comments',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]