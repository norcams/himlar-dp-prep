import pika
import json
import pyramid.httpexceptions as exc

class MQclient(object):

    def __init__(self, config, logger):
        self.log = logger
        self.config = config
        try:
            self.log.info('connect to mq...')
            credentials = pika.PlainCredentials(
                username=self.config['mq_username'],
                password=self.config['mq_password'])
            parameters = pika.ConnectionParameters(
                host=self.config['mq_host'],
                virtual_host=self.config['mq_vhost'],
                credentials=credentials,
                heartbeat_interval=10,
                connection_attempts=2,
                retry_delay=5,
                socket_timeout=10,
                blocked_connection_timeout=30)
            self.connection = pika.BlockingConnection(parameters)
        except Exception as e:
            self.log.error(e)
            raise exc.HTTPInternalServerError("HTTP error occurred.")

    def get_channel(self, queue):
        channel = self.connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel

    def close_connection(self):
        self.log.info('close mq connection')
        self.connection.close()

    def push(self, data, queue='access'):
        channel = self.connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        message = json.dumps(data)
        result = channel.basic_publish(exchange='',
                                       routing_key=queue,
                                       body=message,
                                       properties=pika.BasicProperties(
                                       delivery_mode=2))
        if result:
            self.log.info('New message added to queue: ', queue)
            self.close_connection()
