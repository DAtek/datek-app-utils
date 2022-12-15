from pytest import mark, raises

from datek_app_utils.env_config.types import Bool


class TestBool:
    @mark.parametrize("value", [False, "0", "false", "False", "no", "No"])
    def test_false(self, value, monkeypatch):
        assert Bool(value) is False

    @mark.parametrize("value", [True, "1", "true", "True", "yes", "Yes"])
    def test_true(self, value, monkeypatch):
        assert Bool(value) is True

    def test_invalid(self):
        with raises(ValueError):
            Bool("this is invalid")
