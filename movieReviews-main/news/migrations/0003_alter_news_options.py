# Generated by Django 4.2.4 on 2023-08-26 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]
