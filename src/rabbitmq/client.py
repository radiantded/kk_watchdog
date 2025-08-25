import pika


class RabbitMQClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def _connect(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(self.host, self.port, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        return connection

    def purge_queue(self, queue_name):
        connection = self._connect()
        channel = connection.channel()
        try:
            channel.queue_purge(queue=queue_name)
        except:
            pass
        connection.close()

    def create_channel(self):
        connection = self._connect()
        channel = connection.channel()
        return channel

    def consume(self, queue_name, callback):
        connection = self._connect()
        channel = connection.channel()
        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True
        )
        channel.start_consuming()
        connection.close()

    def produce(self, queue_name, message):
        connection = self._connect()
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange="", routing_key=queue_name, body=message)
        connection.close()
