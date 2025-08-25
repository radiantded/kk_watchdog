from src.tests.test_buy_button.base import BaseBuyButtonTest


class TestBuyButtonGifts(BaseBuyButtonTest):

	BASE_URL = "https://steam.kupikod.com/ru-ru/games/killing-floor-3"
	TEST_ACCOUNT = "https://steamcommunity.com/profiles/76561199559141377"

	def test_gifts(self):
		"""Тест кнопки <Купить> гифтов"""
		self.run()
