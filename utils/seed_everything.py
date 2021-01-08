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