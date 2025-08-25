import sys
from typing import Type

from dotenv import load_dotenv
from pydantic_settings import (
	BaseSettings,
	PydanticBaseSettingsSource,
	SettingsConfigDict,
)


load_dotenv()

DEBUG = sys.platform in ("win32", "darwin")


class Settings(BaseSettings):
	model_config = SettingsConfigDict(env_file=".env")

	# db settings
	db_driver_name: str = "postgresql+asyncpg"
	db_host: str
	db_name: str
	db_user: str
	db_password: str
	db_port: int

	rabbit_host: str
	rabbit_login: str
	rabbit_password: str
	rabbit_virtualhost: str
	rabbit_port: int
	queue_for_tests: str = "tests"

	slack_token: str
	slack_channel: str

	@classmethod
	def settings_customise_sources(
		cls,
		settings_cls: Type[BaseSettings],
		init_settings: PydanticBaseSettingsSource,
		env_settings: PydanticBaseSettingsSource,
		dotenv_settings: PydanticBaseSettingsSource,
		file_secret_settings: PydanticBaseSettingsSource,
	) -> tuple[PydanticBaseSettingsSource, ...]:
		return (
			file_secret_settings,
			env_settings,
			init_settings,
		)


def get_settings() -> Settings:
	return Settings()
