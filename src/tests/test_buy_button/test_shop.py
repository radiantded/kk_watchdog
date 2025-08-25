from src.tests.test_buy_button.base import BaseBuyButtonTest


class TestBuyButtonShop(BaseBuyButtonTest):

	BASE_URL = "https://kupikod.com/shop/killing-floor-3-steam-ru"
	TEST_ACCOUNT = "test@test.ru"

	def _insert_credentials(self):
		self.page.wait_for_timeout(5000)
		self.page.locator("input[id='ui-input-v-0-0-4-0-0']").click()
		self.page.keyboard.insert_text(self.TEST_ACCOUNT)

	def test_shop(self):
		"""Тест кнопки <Купить> шопа"""
		self.run()
