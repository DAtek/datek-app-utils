import os

from pytest import raises

from datek_app_utils.env_config.base import BaseConfig
from datek_app_utils.env_config.errors import InstantiationForbiddenError
from tests.env_config.fixtures import KEY_VOLUME, VolumeConfig


class TestConfig:
    def test_iter(self):
        volume = 5
        os.environ[KEY_VOLUME] = str(volume)

        class Config(VolumeConfig):
            TYPE: str

        items = [item for item in Config]

        assert len(items) == 2
        assert items[0].name == "VOLUME"
        assert items[0].value == volume
        assert items[0].type == int

        assert items[1].name == "TYPE"
        assert items[1].value is None
        assert items[1].type == str

    def test_get(self):
        volume = 10
        os.environ[KEY_VOLUME] = str(volume)

        assert VolumeConfig.VOLUME == volume

    def test_constructor_is_forbidden(self):
        class Config(BaseConfig):
            pass

        with raises(InstantiationForbiddenError):
            Config()
