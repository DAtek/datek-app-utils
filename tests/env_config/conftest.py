from typing import Type

from pytest import fixture
from datek_app_utils.env_config.base import BaseConfig


@fixture(scope="session")
def base_config_class(key_volume) -> Type[BaseConfig]:
    class VolumeConfig(BaseConfig):
        VOLUME: int
        FIELD_WITH_DEFAULT_VALUE: str = "C"
        NON_MANDATORY_FIELD: str = None

    return VolumeConfig


@fixture(scope="session")
def key_volume() -> str:
    return "VOLUME"
