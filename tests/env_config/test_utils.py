from pytest import mark, raises

from datek_app_utils.env_config.errors import (
    ConfigAttributeErrorType,
    ValidationError,
)
from datek_app_utils.env_config.utils import validate_config


class TestValidateConfig:
    def test_ok(self, key_volume, base_config_class, monkeypatch):
        volume = 10
        monkeypatch.setenv(key_volume, str(volume))

        validate_config(base_config_class)

    @mark.parametrize(
        ["volume", "error_type"],
        [
            (None, ConfigAttributeErrorType.NOT_SET),
            ("5.2", ConfigAttributeErrorType.INVALID_VALUE),
        ],
    )
    def test_raise_error(
        self,
        error_type: ConfigAttributeErrorType,
        volume,
        key_volume,
        base_config_class,
        monkeypatch,
    ):
        if volume:
            monkeypatch.setenv(key_volume, str(volume))

        with raises(ValidationError) as exc_info:
            validate_config(base_config_class)

        validation_error = exc_info.value
        assert len(validation_error.errors) == 1
        attribute_error = validation_error.errors[0]

        assert attribute_error.error_type == error_type
        assert attribute_error.attribute_name == key_volume
        assert attribute_error.required_type is int
