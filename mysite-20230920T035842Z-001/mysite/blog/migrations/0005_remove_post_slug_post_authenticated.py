# Generated by Django 4.0 on 2022-02-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
