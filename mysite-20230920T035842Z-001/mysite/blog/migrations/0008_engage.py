# Generated by Django 4.0 on 2022-02-16 08:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_slug_resource_slug_alter_post_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
