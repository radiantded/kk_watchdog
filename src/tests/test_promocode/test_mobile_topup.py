import random

import pytest
from src.tests.test_promocode.base_promocode import BasePromocodeTest


class TestMobileTopup(BasePromocodeTest):

	BASE_URL = "https://kupikod.com/gold/pubg"
	TEST_ACCOUNT = "54234234"

	@pytest.fixture
	def promocode(self) -> str:
		promocodes = self._get_promocodes()["mobile"]
		return random.choice(promocodes)

	# def _open_target_url(self) -> None:
	# 	self.page.goto(self.BASE_URL, wait_until="domcontentloaded")
	# 	self.page.get_by_text("Скопировать промокод").click()

	def _insert_credentials(self):
		self.page.wait_for_timeout(5000)
		self.page.locator('input[id="input-v-0-2-0"]').click()
		self.page.keyboard.insert_text(self.TEST_ACCOUNT)

	def _get_price(self) -> int:
		return int(self.page.locator(
			".ui-details-price__cost"
		).inner_text().split()[0])

	def _insert_promocode(self, promocode: str) -> None:
		self.page.locator('input[id="ui-input-v-0-4"]').fill(promocode)
		self.page.keyboard.press("Enter")
		self.page.wait_for_timeout(5000)

	def test_promocode(self, promocode: str) -> None:
		"""Тест промокодов для мобилок"""
		self.run(promocode)
