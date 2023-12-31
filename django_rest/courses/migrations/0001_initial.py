# Generated by Django 4.2.3 on 2023-11-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('enrolled', models.DateTimeField(auto_now=True)),
                ('semester', models.CharField(choices=[('semester1', 'semester1'), ('semester2', 'semester2'), ('semester3', 'semester3'), ('semester4', 'semester4')], max_length=50)),
                ('mentors_name', models.CharField(max_length=50)),
            ],
        ),
    ]
