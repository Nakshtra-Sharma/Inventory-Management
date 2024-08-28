from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the product_id sequence'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(product_id) FROM invapp_product) WHERE name='invapp_product';")
        self.stdout.write(self.style.SUCCESS('Successfully reset product_id sequence'))
