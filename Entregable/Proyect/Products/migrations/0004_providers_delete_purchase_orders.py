# Generated by Django 4.1.5 on 2023-01-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_category_description_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('provides', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='purchase_orders',
        ),
    ]
