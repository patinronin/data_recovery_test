import asyncio
import inspect
import functools
import time
import logging

def retry(
    max_retries=3,
    delay=1,
    backoff=1,
    exceptions=(Exception,),
    logger=logging.getLogger('app')
):
    """
    Retry decorator with logging support.
    backoff=1 → constant delay
    backoff=2 → exponential backoff
    """


    def decorator(func):
        
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        logger.error(
                            f"[FAILED] {func.__name__} - "
                            f"attempt {attempt}/{max_retries} - Error: {e}"
                        )
                        raise
                    
                    logger.warning(
                        f"[RETRY] {func.__name__} failed on attempt "
                        f"{attempt}/{max_retries} - Error: {e} "
                        f"- Retrying in {current_delay}s"
                    )

                    await asyncio.sleep(current_delay)
                    current_delay *= backoff

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        logger.error(
                            f"[FAILED] {func.__name__} - "
                            f"attempt {attempt}/{max_retries} - Error: {e}"
                        )
                        raise
                    
                    logger.warning(
                        f"[RETRY] {func.__name__} failed on attempt "
                        f"{attempt}/{max_retries} - Error: {e} "
                        f"- Retrying in {current_delay}s"
                    )

                    time.sleep(current_delay)
                    current_delay *= backoff

        # Auto detect async vs sync
        return async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper
    
    return decorator
