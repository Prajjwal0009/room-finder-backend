# Generated by Django 4.2.2 on 2023-06-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', upload_to='uploads/'),
        ),
    ]