from src.tests.test_buy_button.base import BaseBuyButtonTest


class TestBuyButtonMobile(BaseBuyButtonTest):

	BASE_URL = "https://kupikod.com/gold/pubg"
	TEST_ACCOUNT = "5651713251"

	def _expect_popup(self):
		self.page.locator(
			'button[class="base-dialog__close close-btn"]'
		).click()

	def _perform_clicks(self):
		self.page.get_by_role("button", name="Купить").click()

	def test_mobile(self):
		"""Тест кнопки <Купить> мобилок"""
		self.run()
