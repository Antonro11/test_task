# Generated by Django 4.2 on 2023-06-05 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopIndexAnon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.shop')),
            ],
        ),
    ]
