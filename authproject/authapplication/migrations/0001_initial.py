# Generated by Django 5.0 on 2024-01-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
