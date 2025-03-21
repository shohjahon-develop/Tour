# Generated by Django 5.1.4 on 2024-12-29 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_of_Offres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Direct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='index/img')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('price', models.IntegerField()),
                ('bio', models.TextField(blank=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category_of_offres')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.location')),
            ],
        ),
    ]
