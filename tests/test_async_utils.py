from asyncio import Task, all_tasks, sleep
from typing import Set

from pytest import raises

from datek_app_utils.async_utils import async_timeout


class TestAsyncTimeout:
    async def test_returns_result_and_cancels_timeout_task(self):
        @async_timeout(1)
        async def do_something(*args, **kwargs):
            return args, kwargs

        params = ("a", 1)
        kparams = {"fruit": "apple"}

        result = await do_something(*params, **kparams)

        assert result[0] == params
        assert result[1] == kparams
        # only the running test is in the tasks
        assert len(all_tasks()) == 1

    async def test_cancels_timeout_task_on_error(self):
        @async_timeout(1)
        async def raise_error():
            raise RuntimeError

        with raises(RuntimeError):
            await raise_error()

        tasks: Set[Task] = all_tasks()
        for task in tasks:
            assert "raise_timeout_error" not in str(task.get_coro())

    async def test_raises_timeout(self):
        @async_timeout(0.001)
        async def wait():
            await sleep(0.002)

        with raises(TimeoutError):
            await wait()
