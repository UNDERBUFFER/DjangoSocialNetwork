# Generated by Django 3.0.1 on 2020-01-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='./static/photos'),
        ),
    ]
