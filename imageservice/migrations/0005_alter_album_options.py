# Generated by Django 3.2.3 on 2021-05-31 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageservice', '0004_alter_album_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
    ]
