# Generated by Django 4.2.6 on 2023-11-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddffsfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
