# Generated by Django 4.1.2 on 2022-10-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='test_field',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
