# Generated by Django 4.2 on 2023-07-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtBase', '0002_book_contact_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.FileField(upload_to='sketch/'),
        ),
    ]