# Generated by Django 3.2.8 on 2021-10-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='label',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
