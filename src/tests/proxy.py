import random
from typing import Literal, TypeAlias

import requests


Region: TypeAlias = Literal["RU", "UA", "KZ", "UZ"]


class ProxyManager:

	URL = "http://back-hz-3.opl.infrapu.sh:8020/api/v1/proxies"

	def __get_proxies(self, region: Region = "RU") -> dict:
		return requests.get(
			url=self.URL,
			params={
				"region": region,
				"purpose": "universal"
			}
		).json()

	@staticmethod
	def __format_proxy(proxy: dict) -> dict:
		return {
			"server": f"http://{proxy['ip']}:{proxy['port']}",
			"username": f"{proxy['login']}",
			"password": f"{proxy['password']}"
		}

	def get(self) -> dict:
		proxy = random.choice(self.__get_proxies())
		return self.__format_proxy(proxy)
