from src.tests.base import BaseBrowserTest


class BaseBuyButtonTest(BaseBrowserTest):

	PAYMENT_SERVICES = ["tome", "nspk", "oplatum", "kassa", "qr"]

	def _select_country(self):
		"""Метод не используется, если настроены куки"""
		self.page.wait_for_timeout(5000)
		self.page.get_by_text("Выберите регион Steam").click()
		self.page.locator('div[class="select-country"]').click()
		self.page.get_by_text("Россия", exact=True).click()
		self.page.get_by_text("Подтвердить", exact=True).click()
		self.page.wait_for_timeout(5000)

	def _insert_credentials(self):
		"""Метод не используется, если настроены куки"""
		raise NotImplementedError

	def _perform_clicks(self):
		self.page.get_by_role("button", name="Купить").click()

	def _get_predicate(self):
		return lambda response: any(
			response.url.find(s) != -1 for s in self.PAYMENT_SERVICES
		)

	def _expect_redirect(self):
		predicate = self._get_predicate()
		with self.page.expect_request(predicate):
			self._perform_clicks()
			with self.page.expect_response(predicate) as response_event:
				assert response_event.value.status == 200

	def run(self):
		self._open_target_url()
		self._insert_credentials()
		self._expect_redirect()
