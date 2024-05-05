import pika
import time
from datetime import datetime
import json

credentials = pika.PlainCredentials('dima', 'kushchevskyi')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=8080, credentials=credentials)
)

channel = connection.channel()

channel.exchange_declare(exchange='shoes_operator', exchange_type='topic')

channel.queue_declare(queue='A', durable=False)
channel.queue_bind(exchange='shoes_operator', queue='A', routing_key="shoes.sneakers")

channel.queue_declare(queue='B', durable=False)
channel.queue_bind(exchange='shoes_operator', queue='B', routing_key="shoes.running")

channel.queue_declare(queue='C', durable=False)
channel.queue_bind(exchange='shoes_operator', queue='C', routing_key="shoes.*")

def main():
    i = 0
    while True:
        i += 1
        message = {
            "id": i,
            "payload": f"Task #{i}",
            "date": datetime.now().isoformat()
        }

        if i % 2 == 0:
            routing_key = "shoes.sneakers"
        else:
            routing_key = "shoes.running"


        channel.basic_publish(
            exchange='shoes_operator',
            routing_key=routing_key,
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.TRANSIENT_DELIVERY_MODE
            )
        )

        print(" [x] Sent %r" % message)

        time.sleep(1)

    connection.close()


if __name__ == '__main__':
    main()
