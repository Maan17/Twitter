# Generated by Django 3.1.7 on 2022-02-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20220227_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
