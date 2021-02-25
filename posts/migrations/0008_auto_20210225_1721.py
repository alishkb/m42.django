# Generated by Django 3.1.5 on 2021-02-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210225_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_fcat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='fatherCat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scat', to='posts.category', verbose_name='بالا دسته بندی'),
        ),
        migrations.DeleteModel(
            name='FatherCat',
        ),
    ]