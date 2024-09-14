"""Accounts models."""

# Django
from django.contrib.auth.models import AbstractUser

# 3rd-Party
from faker import Faker


class CustomUser(AbstractUser):  # noqa: D101

    @classmethod
    def generate_new_users(cls, users_number=20):
        """Delete all users and create new 'users_number' objects."""

        cls.objects.filter(is_staff=False, is_superuser=False).delete()
        fake = Faker()
        users_to_create = [
            cls(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
            ) for x in range(users_number)
        ]
        cls.objects.bulk_create(users_to_create)
