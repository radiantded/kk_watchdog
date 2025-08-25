import json
from pathlib import Path

from src.tests.base import BaseBrowserTest


class BasePromocodeTest(BaseBrowserTest):

	BASE_URL = None

	@staticmethod
	def _get_promocodes():
		return json.loads(
			Path("./config/promocodes.json").read_text()
		)

	def _insert_credentials(self):
		raise NotImplementedError

	def _insert_promocode(self, promocode: str):
		raise NotImplementedError

	def _get_price(self):
		raise NotImplementedError

	@staticmethod
	def _compare_prices(init: int, promo: int):
		assert int(init) > int(promo)

	def run(self, promocode: str):
		self._open_target_url()
		self._insert_credentials()
		init_price = self._get_price()
		self._insert_promocode(promocode)
		promo_price = self._get_price()
		self._compare_prices(init_price, promo_price)
