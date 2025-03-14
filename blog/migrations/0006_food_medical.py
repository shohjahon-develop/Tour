# Generated by Django 5.1.4 on 2024-12-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_phone_number_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='index/img')),
                ('text', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='index/img')),
                ('text', models.TextField(blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
