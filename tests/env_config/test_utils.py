import os

from pytest import raises, fixture, mark

from datek_app_utils.env_config.errors import (
    ValidationError,
    ConfigAttributeErrorType,
)
from datek_app_utils.env_config.utils import validate_config
from tests.env_config.fixtures import KEY_VOLUME, VolumeConfig


class TestValidateConfig:
    def test_ok(self):
        volume = 10
        os.environ[KEY_VOLUME] = str(volume)

        validate_config(VolumeConfig)

    @mark.parametrize(
        ["volume", "error_type"],
        [
            (None, ConfigAttributeErrorType.NOT_SET),
            ("5.2", ConfigAttributeErrorType.INVALID_VALUE),
        ],
    )
    def test_raise_error(self, error_type: ConfigAttributeErrorType, volume):
        if volume:
            os.environ[KEY_VOLUME] = volume

        with raises(ValidationError) as exc_info:
            validate_config(VolumeConfig)

        validation_error = exc_info.value
        assert len(validation_error.errors) == 1
        attribute_error = validation_error.errors[0]

        assert attribute_error.error_type == error_type
        assert attribute_error.attribute_name == KEY_VOLUME
        assert attribute_error.required_type is int


@fixture(autouse=True)
def clean_env():
    if os.getenv(KEY_VOLUME) is not None:
        del os.environ[KEY_VOLUME]
