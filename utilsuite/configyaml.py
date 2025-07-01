import yaml, os
import numpy as np
from pathlib import Path

class ConfigYAML():
    """
    A configuration helper class for reading from and writing to YAML files.

    This class allows loading a YAML file into instance attributes and saving
    both instance and class attributes back to a YAML file. NumPy arrays are 
    automatically converted to lists when saving to ensure YAML compatibility.

    Methods:
    --------
    load(filename):
        Loads key-value pairs from the YAML file and sets them as instance attributes.

    save(filename):
        Saves instance and class attributes to the specified YAML file.
        Automatically creates the output directory if it doesn't exist.
        NumPy arrays are converted to lists for serialization.
    """
    def __init__(self) -> None:
        pass
    
    def load(self, filename):
        d = yaml.safe_load(Path(filename).read_text())
        for key in d:
            setattr(self, key, d[key])

    def save(self, filename):
        path = filename.rpartition('/')[0]
        if path != '' and not os.path.exists(path):
            os.makedirs(path)
        d = vars(self)
        class_d = vars(self.__class__)
        d_out = {}
        for key in list(class_d.keys()):
            if not (key.startswith('__') or \
                    key.startswith('load') or \
                    key.startswith('save')):
                if isinstance(class_d[key], np.ndarray):
                    d_out[key] = class_d[key].tolist()
                else:
                    d_out[key] = class_d[key]
        for key in list(d.keys()):
            if not (key.startswith('__') or \
                    key.startswith('load') or \
                    key.startswith('save')):
                if isinstance(d[key], np.ndarray):
                    d_out[key] = d[key].tolist()
                else:
                    d_out[key] = d[key]
        with open(filename, 'w+') as ff:
            yaml.dump_all([d_out], ff)
            
