# Generated by Django 3.1.5 on 2021-02-21 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20210221_2122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Disike_Comment',
            new_name='Dislike_Comment',
        ),
        migrations.AlterField(
            model_name='dislike_post',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdislike', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='dislike_post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='udislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like_post',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plike', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='like_post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ulike', to=settings.AUTH_USER_MODEL),
        ),
    ]
