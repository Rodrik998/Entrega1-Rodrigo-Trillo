# Generated by Django 4.1.5 on 2023-01-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_providers_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
