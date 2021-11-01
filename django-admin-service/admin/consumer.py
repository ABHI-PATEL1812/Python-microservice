import json, os, django, pika
from products.models import Product
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters(settings.QUEUE_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("Recieved in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('Start consuming')

channel.start_consuming()

channel.close()

