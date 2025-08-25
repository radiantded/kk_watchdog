from pathlib import Path

from fake_useragent import UserAgent
from playwright.sync_api import Playwright, BrowserContext, Page, sync_playwright, Locator

from config import DEBUG
from src.tests.proxy import ProxyManager


class BaseBrowserTest:

	BASE_URL = None
	DEFAULT_TIMEOUT_MS = 60000

	def setup_method(self) -> None:
		self.pw = sync_playwright().start()
		self.proxy_manager = ProxyManager()
		self.page = self._get_browser_context().new_page()
		self._config_page()

	def _get_browser_context(self) -> BrowserContext:
		self.chrome = self.pw.chromium.launch(
			headless=False if DEBUG else True,
			proxy=self.proxy_manager.get()
		)
		self.context = self.chrome.new_context(
			user_agent=UserAgent(os="Windows").random,
			storage_state=(
				Path(__file__).parent / "test_buy_button" / "config" / "cookies.json"
			)
		)
		return self.context

	@staticmethod
	def _popup_handler(locator: Locator):
		locator.click()

	@staticmethod
	def _order_tooltip_handler(locator: Locator):
		locator.page.locator('div[class="order-status"]').click()

	def _config_page(self) -> None:
		self.page.set_default_timeout(self.DEFAULT_TIMEOUT_MS)
		self.page.set_viewport_size({"height": 1080, "width": 1920})
		self.page.add_locator_handler(
			self.page.get_by_text("Скопировать промокод"),
			self._popup_handler
		)
		self.page.add_locator_handler(
			self.page.locator('div[class="order-tooltip_body"]'),
			self._order_tooltip_handler
		)

	def _open_target_url(self) -> None:
		try:
			self.page.goto(self.BASE_URL, wait_until="load")
		except:
			self.page.goto(self.BASE_URL, wait_until="domcontentloaded")

	def teardown_method(self) -> None:
		self.context.storage_state(
			path=Path(__file__).parent / "test_buy_button" / "config" / "cookies.json"
		)
		self.page.close()
		self.chrome.close()
		self.pw.stop()