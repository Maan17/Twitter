# Generated by Django 3.1.7 on 2022-02-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20220227_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default='0', null=True),
        ),
    ]