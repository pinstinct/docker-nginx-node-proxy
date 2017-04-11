from django.core.management import BaseCommand

from member.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(
            username='hm',
            password='7890uiop',
            email='dev@abc.com',
        )
