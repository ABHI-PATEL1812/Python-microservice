import json

import pika

from django.conf import settings

params = pika.URLParameters(settings.QUEUE_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, data):
    print("heya")
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(data), properties=properties)