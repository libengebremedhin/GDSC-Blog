# Generated by Django 5.0.2 on 2024-02-29 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
