from logging import DEBUG, Formatter

from app_utils.log import LogLevel, LogFormatter, create_logger


def test_debug(caplog):
    message = "message"
    LogLevel.set(DEBUG)
    LogFormatter.set(
        Formatter("%(asctime)s - %(filename)s:%(lineno)d - %(levelname)-8s %(message)s")
    )

    logger = create_logger(__name__)
    logger.debug(message)

    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == DEBUG
    assert message in caplog.messages
