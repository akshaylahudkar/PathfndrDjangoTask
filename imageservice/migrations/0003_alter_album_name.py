# Generated by Django 3.2.3 on 2021-05-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageservice', '0002_auto_20210531_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
