# Generated by Django 4.2.3 on 2023-08-11 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_friend_myself'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='myself',
            options={'ordering': ['-id']},
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_num', models.IntegerField()),
                ('pass_page', models.IntegerField()),
                ('validity', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first_app.person')),
            ],
        ),
    ]
