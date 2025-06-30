import importlib
from typing import Any, TYPE_CHECKING

_lazy_functions = {
    "ConfigYAML": ("configyaml", "ConfigYAML"),
    "Conv2DLayer": ("torch_utils", "Conv2DLayer"),
    "DataProcessor": ("dataprocessor", "DataProcessor"),
    "Dataset": ("torch_utils", "Dataset"),
    "GeodesicLoss": ("rotation_utils", "GeodesicLoss"),
    "LinearLayer": ("torch_utils", "LinearLayer"),
    "ListDict": ("listdict", "ListDict"),
    "Logger": ("logger", "Logger"),
    "Polar2Cartesian": ("jax_utils", "Polar2Cartesian"),
    "PositionalEncoding": ("torch_utils", "PositionalEncoding"),
    "PositionalEncoding_jax": ("jax_utils", "PositionalEncoding_jax"),
    "PositionalEncoding_torch": ("torch_utils", "PositionalEncoding_torch"),
    "Timer": ("timer", "Timer"),
    "TransConv2DLayer": ("torch_utils", "TransConv2DLayer"),
    "_axis_angle_rotation": ("rotation_utils", "_axis_angle_rotation"),
    "angle_w_z": ("rotation_utils", "angle_w_z"),
    "build_lazy_map": ("generate_init", "build_lazy_map"),
    "cholesky_truncated_gaussian_2d_adjusted": ("jax_utils", "cholesky_truncated_gaussian_2d_adjusted"),
    "colorPalette": ("colorpalette", "colorPalette"),
    "coloredText": ("coloredtext", "coloredText"),
    "euler_2_matrix_sincos": ("rotation_utils", "euler_2_matrix_sincos"),
    "extract_top_level_defs": ("generate_init", "extract_top_level_defs"),
    "generate_perms": ("jax_utils", "generate_perms"),
    "get_orient_err": ("rotation_utils", "get_orient_err"),
    "get_posit_err": ("rotation_utils", "get_posit_err"),
    "get_subsample_inds": ("misc", "get_subsample_inds"),
    "keyMonitor": ("keymonitor", "keyMonitor"),
    "load_state": ("jax_utils", "load_state"),
    "mmd_multiscale": ("torch_utils", "mmd_multiscale"),
    "modified_sigmoid": ("misc", "modified_sigmoid"),
    "npprint_suppress": ("misc", "npprint_suppress"),
    "numpify": ("torch_utils", "numpify"),
    "oneLineJaxRNG": ("jax_utils", "oneLineJaxRNG"),
    "open3dUtils": ("open3dutils", "open3dUtils"),
    "plotlyUtils": ("plotlyutils", "plotlyUtils"),
    "pltUtils": ("pltutils", "pltUtils"),
    "qvec2rotmat": ("rotation_utils", "qvec2rotmat"),
    "readTXT": ("misc", "readTXT"),
    "truncated_gaussian_sampler": ("jax_utils", "truncated_gaussian_sampler"),
    "truncated_normal_sampler": ("misc", "truncated_normal_sampler"),
    "uniform_random_rotation": ("rotation_utils", "uniform_random_rotation"),
    "unstack": ("jax_utils", "unstack"),
    "utilitySuite": ("utilitysuite", "utilitySuite"),
}

if TYPE_CHECKING:
    from .configyaml import *
    from .keymonitor import *
    from .coloredtext import *
    from .logger import *
    from .timer import *
    from .dataprocessor import *
    from .colorpalette import *
    from .pltutils import *
    from .listdict import *
    from .utilitysuite import *
    from .misc import *
    from .torch_utils import *
    from .jax_utils import *
    from .rotation_utils import *

def __getattr__(name: str) -> Any:
    if name in _lazy_functions:
        module_name, class_name = _lazy_functions[name]
        module = importlib.import_module(f".{module_name}", __name__)
        cls = getattr(module, class_name)
        globals()[name] = cls  # Cache to avoid repeated getattr calls
        return cls

    raise AttributeError(f"module {__name__} has no attribute {name}")