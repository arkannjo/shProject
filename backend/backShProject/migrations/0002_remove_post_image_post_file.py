# Generated by Django 4.2 on 2023-05-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backShProject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
