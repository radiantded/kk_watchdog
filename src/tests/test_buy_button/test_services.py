from src.tests.test_buy_button.base import BaseBuyButtonTest


class TestServicesBuyButton(BaseBuyButtonTest):

	BASE_URL = "https://kupikod.com/console/ps-store"
	TEST_ACCOUNT = "test@test.ru"

	def _open_target_url(self) -> None:
		self.page.goto(self.BASE_URL, wait_until="domcontentloaded")
		self.page.locator('span[class="btn__wrapper"]', has_text="Купить").wait_for()

	def _insert_email(self):
		self.page.locator(
			'div[class="ui-text-field__wrapper"]',
			has_text="Логин PlayStation"
		).locator("input").click()
		self.page.wait_for_timeout(1000)
		self.page.keyboard.insert_text(self.TEST_ACCOUNT)

	def _click_email_toggle_button(self):
		self.page.locator(
			"div[class='flex mt-[14px] gap-3']",
			has_text="Email совпадает с логином PSN"
		).locator('div[class="tgl-btn"]').click()
		self.page.wait_for_timeout(1000)

	def _insert_credentials(self):
		self._insert_email()
		self.page.wait_for_timeout(1000)
		self._click_email_toggle_button()

	def test_services(self):
		"""Тест кнопки <Купить> консолей и сервисов"""
		self.run()
