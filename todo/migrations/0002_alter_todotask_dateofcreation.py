# Generated by Django 4.1.7 on 2023-03-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='dateOfCreation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
