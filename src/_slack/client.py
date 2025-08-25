import os
import ssl

import certifi
import slack

from config import get_settings
from src.types import Report


class SlackClient:

	def __init__(self):
		settings = get_settings()
		self.channel = os.getenv("slack_channel")
		self.instance = slack.WebClient(
			token=settings.slack_token,
			ssl=ssl.create_default_context(cafile=certifi.where())
		)

	@staticmethod
	def _fail_message(report: Report):
		return (
			"@here\n"
			f"❌ *FAIL*: `{report.test_name}`\n"
			f"> File: `{report.nodeid}`\n"
			f"> Error: ```{report.error_msg}```"
		)

	@staticmethod
	def _success_message(report: Report):
		return f"✅ *PASS*: `{report.test_name}`"


	def send_message(self, report: Report):
		message = (
			self._fail_message(report) if report.error_msg
			else self._success_message(report)
		)
		self.instance.chat_postMessage(
			link_names=1,
			channel=self.channel,
			text=f"```{message}```"
		)


slack_client = SlackClient()
