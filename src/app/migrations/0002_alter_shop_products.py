# Generated by Django 4.2 on 2023-06-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='products',
            field=models.ManyToManyField(null=True, related_name='product', to='app.product'),
        ),
    ]