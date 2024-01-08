# Generated by Django 4.0.6 on 2022-07-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='slug',
            field=models.SlugField(default='slug', max_length=60, unique=True),
            preserve_default=False,
        ),
    ]
