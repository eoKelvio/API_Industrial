# Generated by Django 5.0.3 on 2024-03-14 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryEntity',
            new_name='Entity',
        ),
    ]