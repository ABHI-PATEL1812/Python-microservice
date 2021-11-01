import json

import pika

params = pika.URLParameters('secret_ampq_key')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, data):
    print('heyyaaaaa')
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(data), properties=properties)