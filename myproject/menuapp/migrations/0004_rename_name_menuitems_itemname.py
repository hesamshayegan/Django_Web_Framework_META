# Generated by Django 5.0 on 2023-12-26 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0003_rename_course_menuitems_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='name',
            new_name='itemname',
        ),
    ]
