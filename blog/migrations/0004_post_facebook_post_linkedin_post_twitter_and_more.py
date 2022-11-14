# Generated by Django 4.1.1 on 2022-11-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='facebook',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='linkedin',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='twitter',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]