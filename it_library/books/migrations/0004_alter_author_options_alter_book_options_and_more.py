# Generated by Django 4.1.2 on 2022-10-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_options_remove_book_test_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id', 'fullname'], 'verbose_name': 'Автор', 'verbose_name_plural': 'Автори'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id', 'title', 'price'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id', 'title'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, verbose_name='Біофграфія автора'),
        ),
    ]
