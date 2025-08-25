from src._slack.client import slack_client
from src.db.queries import TestResults
from src.types import Report


def pytest_runtest_makereport(item, call):
	"""Хук, вызывается после каждого этапа выполнения теста"""
	if call.when == "call":
		report = Report(
			test_name=item.function.__doc__ or item.name,
			nodeid=item.nodeid,
			error_msg=str(call.excinfo.value) if call.excinfo else None,
			status="fail" if call.excinfo else "success"
		)
		slack_client.send_message(report)
		with TestResults() as queries:
			queries.update(report)
