# Generated by Django 5.0 on 2024-01-14 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameIndex(
            model_name='book',
            new_name='BookListAPI_price_779a55_idx',
            old_name='BookListAPI_price_f504e4_idx',
        ),
    ]