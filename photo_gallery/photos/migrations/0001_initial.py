# Generated by Django 4.0.6 on 2022-07-23 14:15

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('large_image', imagekit.models.fields.ProcessedImageField(upload_to='photos', verbose_name='image file')),
            ],
        ),
    ]
