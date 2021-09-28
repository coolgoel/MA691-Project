# Generated by Django 3.2.7 on 2021-09-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=18)),
                ('sex', models.CharField(default='Male', max_length=10)),
                ('bmi', models.FloatField(default=24.0)),
                ('children', models.IntegerField(default=False)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
    ]
