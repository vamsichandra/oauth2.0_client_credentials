# Generated by Django 4.0.1 on 2023-03-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
