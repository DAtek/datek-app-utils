from asyncio import sleep
from logging import ERROR

from pytest import mark, raises
from datek_app_utils.async_utils import AsyncWorker, async_timeout
from datek_app_utils.log import create_logger


class TestAsyncWorker:
    @mark.asyncio
    @async_timeout(0.1)
    async def test_worker_finishes_successfully(self):
        worker = ExampleWorker()
        worker.start()
        await worker

    @mark.asyncio
    @async_timeout(0.1)
    async def test_worker_handles_error_successfully(self, caplog):
        worker = ExampleWorker(raise_error=True)
        worker.start()

        await worker

        assert caplog.records
        log_record = caplog.records[0]
        assert log_record.levelno == ERROR
        assert isinstance(log_record.msg, RuntimeError)
        assert log_record.msg.args == (ExampleWorker.ERROR_MESSAGE,)

    @mark.asyncio
    @async_timeout(0.1)
    async def test_worker_runs_forever(self):
        worker = ExampleWorker(run_forever=True)
        worker.start()
        await worker.wait_started()

        @async_timeout(0.05)
        async def wait_for_worker():
            await worker

        with raises(TimeoutError):
            await wait_for_worker()


class ExampleWorker(AsyncWorker):
    ERROR_MESSAGE = "LOL"

    def __init__(self, raise_error: bool = False, run_forever: bool = False):
        super().__init__()
        self._raise_error = raise_error
        self._should_run_forever = run_forever
        self._logger = create_logger(self.__class__.__name__)

    async def run(self):
        await sleep(0.01)

        if self._raise_error:
            raise RuntimeError(self.ERROR_MESSAGE)

        if self._should_run_forever:
            return

        await self.stop()

    async def handle_error(self, error: Exception):
        self._logger.error(error)
        self.stop()
