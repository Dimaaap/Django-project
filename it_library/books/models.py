from django.db import models
from django.contrib.postgres.indexes import GinIndex


class Category(models.Model):
    title = models.CharField(max_length=70, verbose_name='Назва')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id', 'title']


class Author(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Повне ім'я автора")
    biography = models.TextField(blank=True, verbose_name='Біофграфія автора')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
        ordering = ['id', 'fullname']


class Book(models.Model):
    UKRAINIAN = 'Ukr'
    PIGGEST = 'Rus'
    ENGLISH = 'Eng'
    POSSIBLE_LANGUAGES_OF_PUB_OF_THE_BOOKS = [
        (UKRAINIAN, 'Українська'),
        (PIGGEST, 'Свиняча'),
        (ENGLISH, 'Англійська')
    ]

    title = models.CharField(max_length=150, verbose_name='Назва книги')
    language = models.CharField(max_length=3, choices=POSSIBLE_LANGUAGES_OF_PUB_OF_THE_BOOKS,
                                default=UKRAINIAN, verbose_name='Мова видання')
    description = models.TextField(blank=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Ціна')
    authors = models.ManyToManyField(Author, verbose_name='Автори')
    categories = models.ManyToManyField(Category, verbose_name='Категорії')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Зображення', blank=True)
    content = models.FileField(upload_to='content/%Y/%m/%d', verbose_name='Контент', blank=True)
    chunk_title = models.TextField(blank=True, verbose_name="Розбита назва книги: ")

    @staticmethod
    def split_title(string_for_chunk: str):
        """
        Розбиває нахву книги,додаючи до кожного слова новий сисмвол на кожній ітерації
        Наприклад
        string_for_chunk = "Укус Python"
        return Уку Уку Pyt Pyth Pytho Pytho Укус Python
        """
        chunk_list = []
        split_string = string_for_chunk.split()
        split_string_more_3 = [i for i in split_string if len(i) >= 3]
        for index, word in enumerate(split_string_more_3):
            for word_index, _ in enumerate(word):
                chunk_list.append(word[:word_index])
        chunk_list = [i for i in chunk_list if len(i) >= 3]
        final_string = f'{" ".join(chunk_list)} {" ".join(split_string)}'
        return final_string

    def save(self, *args, **kwargs):
        self.chunk_title = self.split_title(str(self.title))
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['id', 'title', 'price']
        indexes = [
            GinIndex(fields=["title"])
        ]

    def get_authors(self):
        return '\n'.join([b.fullname for b in self.authors.all()])

    def get_categories(self):
        return '\n'.join([i.title for i in self.categories.all()]).split()[0]

    def get_categories_id(self):
        return '\n'.join([str(i.pk) for i in self.categories.all()])[0]

    def get_full_categories(self):
        iter_categories = iter(i.title for i in self.categories.all())
        yield next(iter_categories)
