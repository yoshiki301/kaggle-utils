# timer
import time
import logging
from typing import Optional
from contextlib import contextmanager

@contextmanager
def timer(name: str, logger: Optional[logging.Logger] = None):
    """
    If you use logger, you must define logger object globaly.
    """
    t0 = time.time()
    yield
    msg = f"[{name}] done in {time.time()-t0:.0f} [s]"
    if logger:
        logger.info(msg)
    else:
        print(msg)