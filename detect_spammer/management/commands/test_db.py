import random
from django.core.management.base import BaseCommand
from faker import Faker
from detect_spammer.models import DetectSpammer, Spam

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_users = 200
        num_spam_entries = 250

        for _ in range(num_users):
            DetectSpammer.objects.create(
                name=fake.name(),
                phone_number=fake.phone_number(),
                email=fake.email()
            )

        phone_numbers = [fake.phone_number() for _ in range(num_spam_entries)]
        for phone_number in phone_numbers:
            user = random.choice(DetectSpammer.objects.all())
            Spam.objects.create(
                phone_number=phone_number,
                reported_by=user
            )


