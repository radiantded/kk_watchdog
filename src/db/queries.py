from src.db.conn import DatabaseConnection
from src.types import Report


class TestModules(DatabaseConnection):

	def get_all(self) -> list[tuple[int, str]]:
		cursor = self.conn.cursor()
		cursor.execute(
			"""
				SELECT id, command
				FROM tests.modules
				WHERE queued_at < NOW() - (INTERVAL '1 second' * interval_seconds)
				   OR queued_at IS NULL
				ORDER BY queued_at NULLS FIRST
			"""
		)
		return cursor.fetchall()

	def update_queued_at(self, module_id: int) -> None:
		cursor = self.conn.cursor()
		cursor.execute(
			"""
				UPDATE tests.modules
				SET queued_at = NOW()
				WHERE id = %s
			""",
			(module_id, ),
		)
		self.conn.commit()


class TestResults(DatabaseConnection):

	def update(self, report: Report):
		cursor = self.conn.cursor()
		cursor.execute(
			"""
				INSERT INTO tests.results (command, status) 
				VALUES (%s, %s)
			""",
			(report.nodeid.split("::")[0], report.status),
		)
		self.conn.commit()
