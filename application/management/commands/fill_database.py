# myapp/management/commands/add_fake_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from application.models import Author, Book, Publisher
from random import randint, sample


class Command(BaseCommand):
    help = "Add fake data to Author and Book tables"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Adding 1000 fake authors
        for _ in range(1000):
            name = fake.name()
            age = randint(20, 80)
            Author.objects.create(name=name, age=age)

        # Getting all authors from the database
        authors = Author.objects.all()

        # Adding 1500 fake books
        for _ in range(1500):
            name = fake.catch_phrase()
            pages = randint(100, 1000)
            price = round(randint(500, 5000) / 100, 2)  # Random price between 5 and 50
            rating = round(randint(1, 50) / 10, 1)  # Random rating between 0.1 and 5.0
            author_list = sample(list(authors), randint(1, 3))  # Randomly select 1 to 3 authors
            pubdate = fake.date_this_century()

            # Create or get a random Publisher
            publisher_name = fake.company()
            publisher, _ = Publisher.objects.get_or_create(name=publisher_name)

            book = Book.objects.create(
                name=name,
                pages=pages,
                price=price,
                rating=rating,
                publisher=publisher,  # Assign the publisher to the book
                pubdate=pubdate,
            )
            book.authors.set(author_list)  # Assign randomly selected authors to the book
