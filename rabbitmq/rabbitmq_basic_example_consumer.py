import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def main():
    credentials = pika.PlainCredentials('dima', 'kushchevskyi')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=8080, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='hello_world')
    channel.basic_consume(
        queue='hello_world', on_message_callback=callback, auto_ack=True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
