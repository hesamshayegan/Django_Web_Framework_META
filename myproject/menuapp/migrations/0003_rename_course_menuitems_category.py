# Generated by Django 5.0 on 2023-12-26 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0002_menuitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='course',
            new_name='category',
        ),
    ]
