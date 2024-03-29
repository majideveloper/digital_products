# Generated by Django 4.2 on 2024-01-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='creates_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='creates_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='creates_time',
            new_name='created_time',
        ),
        migrations.AlterField(
            model_name='category',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='categories/'),
        ),
    ]
