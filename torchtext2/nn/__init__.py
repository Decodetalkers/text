import warnings
import torchtext2
if torchtext2._WARN:
    warnings.warn(torchtext2._TORCHTEXT_DEPRECATION_MSG)

from .modules import *  # noqa: F401,F403
