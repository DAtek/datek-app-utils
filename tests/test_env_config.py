import os
from functools import wraps
from logging import INFO, ERROR

from pytest import raises

from app_utils.env_config import BaseConfig, InstantiationForbiddenError, validate_config

KEY_VOLUME = "VOLUME"


def reset_value(key: str):
    def decorator(function: callable):
        @wraps(function)
        def wrapper(*args, **kwargs):
            original_value = os.getenv(key)
            result = function(*args, **kwargs)

            if original_value is not None:
                os.environ[key] = original_value
                return result

            if os.environ.get(key) is not None:
                del os.environ[key]

            return result

        return wrapper

    return decorator


class TestConfig:
    @reset_value(KEY_VOLUME)
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

    @reset_value(KEY_VOLUME)
    def test_get(self):
        volume = 10
        os.environ[KEY_VOLUME] = str(volume)

        assert VolumeConfig.VOLUME == volume

    def test_constructor_is_forbidden(self):
        class Config(BaseConfig):
            pass

        with raises(InstantiationForbiddenError):
            Config()


class TestValidateConfig:
    @reset_value(KEY_VOLUME)
    def test_value_in_log_info(self, caplog):
        volume = 10
        os.environ[KEY_VOLUME] = str(volume)

        assert validate_config(VolumeConfig)

        assert len(caplog.records) == 2
        assert caplog.records[0].levelno == INFO
        assert VolumeConfig.__name__ in caplog.records[0].message

        assert caplog.records[1].levelno == INFO
        assert caplog.records[1].message == f"VOLUME: {VolumeConfig.VOLUME}"

    @reset_value(KEY_VOLUME)
    def test_log_error_if_value_is_none(self, caplog):
        if os.getenv(KEY_VOLUME) is not None:
            del os.environ[KEY_VOLUME]

        assert not validate_config(VolumeConfig)
        assert caplog.records[1].levelno == ERROR
        assert f"{int}" in caplog.records[1].message

    @reset_value(KEY_VOLUME)
    def test_log_error_if_value_is_wrong_type(self, caplog):
        os.environ[KEY_VOLUME] = "5.3"

        assert not validate_config(VolumeConfig)
        assert caplog.records[1].levelno == ERROR


class VolumeConfig(BaseConfig):
    VOLUME: int
