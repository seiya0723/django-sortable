# Generated by Django 4.2.7 on 2024-03-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='sort',
            field=models.IntegerField(default=1, verbose_name='並び順'),
            preserve_default=False,
        ),
    ]
