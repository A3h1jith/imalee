# Generated by Django 4.2 on 2023-04-14 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imaleephotographs', '0003_alter_category_options_alter_gallery_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='category',
            new_name='Category',
        ),
    ]
