import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    credentials = pika.PlainCredentials('dima', 'kushchevskyi')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=8080, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='B', durable=False)
    channel.basic_consume(queue='B', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
