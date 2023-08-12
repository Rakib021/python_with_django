# Generated by Django 4.2.3 on 2023-08-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('take_interview', models.BooleanField()),
                ('hiring', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.RemoveField(
            model_name='managermodel',
            name='employeemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='passport',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
        migrations.DeleteModel(
            name='Me',
        ),
        migrations.AlterField(
            model_name='studentinfomodel',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='studentinfomodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='teacherinfomodel',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='teacherinfomodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='EmployeeModel',
        ),
        migrations.DeleteModel(
            name='ManagerModel',
        ),
        migrations.DeleteModel(
            name='Passport',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]