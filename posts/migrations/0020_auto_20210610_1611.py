# Generated by Django 3.1.5 on 2021-06-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20210610_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='posts.Tag', verbose_name='برچسب'),
        ),
    ]
