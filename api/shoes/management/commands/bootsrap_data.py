from django.core.management.base import BaseCommand, CommandError
from api.shoes.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = 'Adds initial data for shoes.models.ShoeType and shoes.models.ShoeColor' # noqa
    COLORS = ['red', 'orange', 'yellow', 'green',
              'blue', 'indigo', 'violet', 'black', 'white']
    TYPES = ['sneaker', 'boot', 'sandal', 'dress', 'other']

    def handle(self,  *args, **kwargs):
        for c in self.COLORS:
            ShoeColor.objects.create(name=c)

        for t in self.TYPES:
            ShoeType.objects.create(style=t)

        self.stdout.write(self.style.SUCCESS(
            'Successfully imported seed data'))
