import pika 

def main():
    # Спочатку нам потрібно створити з'єднання з RabbitMQ:
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
    channel = connection.channel()

    # За замовчуванням користувач для Docker-контейнера має нікнейм guest з паролем guest. 
    # В результаті в змінній channel ми отримуємо Channel.

    # Далі потрібно створити чергу повідомлень і дамо їй ім'я 'hello_world':
    channel.queue_declare(queue="hello_world")

    # RabbitMQ проігнорує повідомлення, якщо воно відправлене в неіснуючу чергу. 
    # Далі надсилаємо саме повідомлення:
    channel.basic_publish(exchange="", routing_key="hello_world", body="Hello world!".encode())
    # Тут ми вказали exchange порожнім рядком, у цьому випадку RabbitMQ буде використовувати 
    # біржу за замовчуванням (AMQP default) типу direct. Повідомлення надсилаються в чергу, 
    # ім'я якої суворо збігається з routing_key.

    print(" [x] Sent 'Hello World!'")

    # Після відправлення потрібно обов'язково закрити з'єднання:
    connection.close()


if __name__ == '__main__':
    main()


