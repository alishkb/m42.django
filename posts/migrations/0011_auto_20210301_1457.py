# Generated by Django 3.1.5 on 2021-03-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210301_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('name',), 'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
    ]
