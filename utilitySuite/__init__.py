import importlib
from typing import Any, TYPE_CHECKING

__all__ = ["ConfigYAML", 
           "keyMonitor",
           'coloredText',
           "Logger",
           "Timer",
           "DataProcessor",
           "colorPalette",
           "pltUtils",
           "ListDict",
           "utilitySuite"]

if TYPE_CHECKING:
    from .configyaml import ConfigYAML
    from .keymonitor import keyMonitor
    from .coloredtext import coloredText
    from .logger import Logger
    from .timer import Timer
    from .dataprocessor import DataProcessor
    from .colorpalette import colorPalette
    from .pltutils import pltUtils
    from .listdict import ListDict
    from .utilitysuite import utilitySuite

def __getattr__(name: str) -> Any:
    class_to_module = {
        cls: (cls.lower(), cls) for cls in __all__
    }

    if name in class_to_module:
        module_name, class_name = class_to_module[name]
        module = importlib.import_module(f".{module_name}", __name__)
        cls = getattr(module, class_name)
        globals()[name] = cls  # Cache to avoid repeated getattr calls
        return cls

    raise AttributeError(f"module {__name__} has no attribute {name}")