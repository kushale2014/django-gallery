# Generated by Django 3.0.2 on 2020-02-17 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20200217_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_name',
        ),
    ]