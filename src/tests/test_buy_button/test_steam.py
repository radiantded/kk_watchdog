from src.tests.test_buy_button.base import BaseBuyButtonTest


class TestSteamBuyButton(BaseBuyButtonTest):

	BASE_URL = "https://steam.kupikod.com/"
	TEST_ACCOUNT = "TEST"

	def _insert_credentials(self):
		self.page.wait_for_timeout(5000)
		self.page.locator("div[data-testid='login']").click()
		self.page.keyboard.insert_text(self.TEST_ACCOUNT)

	def _perform_clicks(self):
		self.page.get_by_role("button", name="Купить").click()
		self.page.get_by_text("Продолжить без регистрации").click()

	def test_steam(self):
		"""Тест кнопки <Купить> пополняшки Steam"""
		self.run()