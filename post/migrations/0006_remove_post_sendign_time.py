# Generated by Django 3.1.5 on 2021-02-04 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sendign_time',
        ),
    ]
