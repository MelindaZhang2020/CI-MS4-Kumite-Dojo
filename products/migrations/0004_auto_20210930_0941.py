# Generated by Django 3.2.7 on 2021-09-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizes', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='products.Size'),
        ),
    ]
