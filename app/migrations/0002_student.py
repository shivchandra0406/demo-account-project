# Generated by Django 3.2.7 on 2021-10-05 17:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('pid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('roll_no', models.IntegerField()),
                ('mobile_no', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
