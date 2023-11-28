from django.core.management.base import BaseCommand
from geonode.base.models import ResourceBase


class Command(BaseCommand):
    help = 'Count how many resource are available'

    def add_arguments(self, parser):
        parser.add_argument('resource_type', type=str)

    def handle(self, *args, **options):
        counter = ResourceBase.objects.filter(resource_type=options['resource_type']).count()
        self.stdout.write(self.style.SUCCESS('Total resource found "%s"' % counter))
