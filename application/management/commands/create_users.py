from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Create n random users"

    def add_arguments(self, parser):
        parser.add_argument("input_count", type=int, choices=range(1, 11), help="Number of users to create (1-10)")

    def handle(self, *args, **options):
        input_count = options["input_count"]
        fake = Faker()

        User.objects.bulk_create(
            User(username=fake.user_name(), email=fake.email(), password=User.objects.make_random_password())
            for _ in range(input_count)
        )

        self.stdout.write(self.style.SUCCESS(f"Successfully created {input_count} random users"))
