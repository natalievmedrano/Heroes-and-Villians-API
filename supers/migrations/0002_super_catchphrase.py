# Generated by Django 4.1.5 on 2023-03-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='catchphrase',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
