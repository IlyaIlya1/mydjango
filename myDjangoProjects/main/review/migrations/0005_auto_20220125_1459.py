# Generated by Django 3.2.4 on 2022-01-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20211210_0915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='review',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='Контент'),
        ),
    ]