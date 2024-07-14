# Generated by Django 4.2.14 on 2024-07-14 18:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=225, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narxi')),
                ('duration', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sayohat davomiyligi')),
                ('group', models.CharField(blank=True, max_length=50, null=True, verbose_name='Guruh')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', related_query_name='plan', to='tour.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TourGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='galleries/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', related_query_name='gallery', to='tour.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
