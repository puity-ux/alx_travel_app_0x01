from django.core.management.base import BaseCommand
from listings.models import Listing  # or your actual models
from faker import Faker

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.company(),
                description=fake.text(),
                location=fake.city(),
                price=fake.random_number(digits=5),
                available=True
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))