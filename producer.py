import pika
import time

# cloudamql.com parameters
url = "amqp://ppwsmmng:HpG2D1_3oUHWqcbcIhhXjsZ5a_s4uAp3@jellyfish.rmq.cloudamqp.com/ppwsmmng"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.basic_publish(exchange="test-exchange", mandatory=True,
                      routing_key="routing-key",
                      body="hello world!!!!!!!!!!!!!")
print("Mensagem enviada")
connection.close()