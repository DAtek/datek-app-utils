from datek_app_utils.env_config.errors import (
    ConfigAttributeError,
    ConfigAttributeErrorType,
)


class TestConfigAttributeError:
    def test_repr(self):
        error = ConfigAttributeError(
            ConfigAttributeErrorType.INVALID_VALUE, "unit", float
        )

        assert repr(error) == f"{error.attribute_name}: {error.error_type}"

    def test_str(self):
        error = ConfigAttributeError(
            ConfigAttributeErrorType.INVALID_VALUE, "unit", float
        )

        assert (
            str(error)
            == f"{error.attribute_name}: {error.error_type}. Required type: {error.required_type}"
        )
