# Generated by Django 3.1.5 on 2021-06-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20210310_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Tag', verbose_name='برچسب'),
        ),
    ]
