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

# seed_everything
import os
import sys
import random

import numpy as np
import tensorflow as tf
import torch

def seed_everything(seed: int=2021):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    if "numpy" in sys.modules:
        np.random.seed(seed)
    if "tensorflow" in sys.modules:
        tf.random.set_seed(seed)
    if "torch" in sys.modules:
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
