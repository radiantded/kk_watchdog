import json
import subprocess
import time

from config import Settings
from src.db.queries import TestModules
from src.rabbitmq.client import RabbitMQClient


class Watchdog:

	def __init__(self, settings: Settings):
		self.settings = settings
		self._rmq_client = RabbitMQClient(
			host=settings.rabbit_host,
			port=settings.rabbit_port,
			username=settings.rabbit_login,
			password=settings.rabbit_password,
		)
		self._test_queries = TestModules

	@staticmethod
	def test_callback(channel, method, properties, body):
		message: dict = json.loads(body.decode())
		print(message)
		result = subprocess.run(
			["pytest", message["command"]], capture_output=True, text=True
		)
		stdout = result.stdout
		stderr = result.stderr
		returncode = result.returncode

		print("STDOUT:\n", stdout[-500:])
		if returncode != 0:
			print("STDERR:\n", stderr)

	def produce(self):
		while True:
			try:
				with self._test_queries() as queries:
					tests = queries.get_all()
					self._rmq_client.purge_queue(queue_name=self.settings.queue_for_tests)
					for _id, command in tests:
						self._rmq_client.produce(
							queue_name=self.settings.queue_for_tests,
							message=json.dumps({
								"module_id": _id,
								"command": command
							}),
						)
						queries.update_queued_at(_id)
			finally:
				time.sleep(5)

	def consume(self):
		self._rmq_client.consume(
			queue_name=self.settings.queue_for_tests,
			callback=self.test_callback
		)
