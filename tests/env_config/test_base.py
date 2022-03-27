from pytest import raises

from datek_app_utils.env_config.base import BaseConfig
from datek_app_utils.env_config.errors import InstantiationForbiddenError


class SomeOtherMixinWhichDoesntRelateToEnvConfig:
    color = "red"


class TestConfig:
    def test_iter(self, monkeypatch, key_volume, base_config_class):
        volume = 5
        monkeypatch.setenv(key_volume, str(volume))

        class Config(SomeOtherMixinWhichDoesntRelateToEnvConfig, base_config_class):
            TYPE: str

        items = [item for item in Config]

        assert len(items) == 5
        assert Config.color == "red"

        assert items[0].name == "TYPE"
        assert items[0].value is None
        assert items[0].type == str

        assert items[1].name == "FIELD_WITH_DEFAULT_VALUE"
        assert items[1].value == "C"
        assert items[1].type == str

        assert items[2].name == "NON_MANDATORY_FIELD"
        assert items[2].value is None
        assert items[2].type == str

        assert items[3].name == "TYPED_NON_MANDATORY_FIELD"
        assert items[3].value is None
        assert items[3].type == str

        assert items[4].name == "VOLUME"
        assert items[4].value == volume
        assert items[4].type == int

    def test_get(self, monkeypatch, key_volume, base_config_class):
        volume = 10
        monkeypatch.setenv(key_volume, str(volume))

        assert getattr(base_config_class, "VOLUME") == volume

    def test_constructor_is_forbidden(self):
        class Config(BaseConfig):
            pass

        with raises(InstantiationForbiddenError):
            Config()
