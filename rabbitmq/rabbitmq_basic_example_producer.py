import pika

def main():
    credentials = pika.PlainCredentials('dima', 'kushchevskyi')

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost', port=8080, credentials=credentials)
    )

    channel = connection.channel()

    channel.queue_declare(queue='hello_world')

    channel.basic_publish(
        exchange='', routing_key='hello_world', body='Hello world!'.encode()
    )

    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    main()
