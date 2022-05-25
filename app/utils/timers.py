import asyncio

TASKS = {}


def set_timeout(callable, timeout, *args, **kwargs):
    task = asyncio.create_task(
        exec_timeout(callable, timeout, *args, **kwargs)
    )
    # TODO: return timeout id
    return task


def set_interval(callable, interval, *args, **kwargs):
    task = asyncio.create_task(
        exec_interval(callable, interval, *args, **kwargs)
    )
    # TODO: return interval id
    return task


async def exec_timeout(callable, timeout, *args, **kwargs):
    await asyncio.sleep(timeout)
    call = callable(*args, **kwargs)
    if asyncio.iscoroutine(call):
        return await call
    else:
        return call


async def exec_interval(callable, interval, *args, **kwargs):
    while True:
        await asyncio.sleep(interval)
        call = callable(*args, **kwargs)
        if asyncio.iscoroutine(call):
            await call

# TODO Clear interval and clear timeout
