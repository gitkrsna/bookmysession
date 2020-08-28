# Generated by Django 3.1 on 2020-08-28 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=60)),
                ('email_id', models.EmailField(max_length=50)),
                ('child_name', models.CharField(max_length=50)),
                ('child_age', models.IntegerField()),
                ('course_time_date', models.CharField(max_length=50)),
            ],
        ),
    ]