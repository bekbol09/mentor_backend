# Generated by Django 4.2.4 on 2023-08-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/announcement/'),
        ),
    ]
