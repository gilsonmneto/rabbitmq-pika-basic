import pika
import time

# cloudamql.com parameters
url = "amqp://ppwsmmng:HpG2D1_3oUHWqcbcIhhXjsZ5a_s4uAp3@jellyfish.rmq.cloudamqp.com/ppwsmmng"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue="test-queue")


def callback(ch, method, properties, body):
    print("Received %r" % body)
    # acknowledgement
    time.sleep(40)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Confirmação de recebimento enviada")


channel.basic_consume(queue='test-queue', on_message_callback=callback)
print("Waiting for messages")
channel.start_consuming()
