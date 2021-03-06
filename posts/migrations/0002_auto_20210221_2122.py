# Generated by Django 3.1.5 on 2021-02-21 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like_comment',
            name='selection',
        ),
        migrations.RemoveField(
            model_name='like_post',
            name='selection',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_likes',
        ),
        migrations.CreateModel(
            name='Dislike_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ناپسند پست',
                'verbose_name_plural': 'ناپسند پست ها',
            },
        ),
        migrations.CreateModel(
            name='Disike_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ناپسند نظر',
                'verbose_name_plural': 'ناپسند نظر ها',
            },
        ),
    ]
