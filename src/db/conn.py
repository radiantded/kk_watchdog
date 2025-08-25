import psycopg

from config import Settings


class DatabaseConnection:

	def __init__(self):
		settings = Settings()
		self.host = settings.db_host
		self.port = settings.db_port
		self.user = settings.db_user
		self.password = settings.db_password
		self.dbname = settings.db_name
		self.conn = None

	def __enter__(self) -> "DatabaseConnection":
		self.conn = psycopg.connect(
			host=self.host,
			port=self.port,
			user=self.user,
			password=self.password,
			dbname=self.dbname,
		)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb) -> None:
		self.conn.close()
