import sys
import pika
import json
from datetime import datetime

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange="task_mock", exchange_type="direct")
channel.queue_declare(queue="task_queue", durable=True)
channel.queue_bind(exchange="task_mock", queue="task_queue")
# Коли RabbitMQ завершує роботу звичайним чином або аварійно, він забуває про черги та повідомлення. 
# Щоб такої ситуації не відбувалося, нам необхідно вказати прапор durable=True 
# під час визначення черги.

def main():

    # Ми формуємо якийсь словник message і додаємо до нього імітацію корисного навантаження.
    # І відправляємо повідомлення на біржу, попередньо запакувавши його 
    # в байт-рядок json.dumps(message).encode():
    for i in range(5):
        message = {
            "id": i + 1,
            "payload": f"Task #{i + 1}",
            "date": datetime.now().isoformat()
        }

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
    connection.close()
    # delivery_mode=pika.spec.TRANSIENT_DELIVERY_MODE - не зберігати повід-ня та працює швидше.
    # delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE - зберігати повідомлення на диску, 
        # повільніше, але надійніше, та використовується майже завжди.
    
if __name__ == '__main__':
    main()
