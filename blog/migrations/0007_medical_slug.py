# Generated by Django 5.1.4 on 2024-12-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_food_medical'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
