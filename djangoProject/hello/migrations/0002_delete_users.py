# Generated by Django 4.1.3 on 2022-12-07 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users',
        ),
    ]