import numpy as np
class ListDict:
    """
    A simple container class that manages multiple named lists as attributes,
    with convenient methods to initialize, manipulate, save, and load them.

    Key Features:
    - Initialize multiple empty lists by key names.
    - Access keys as attributes and get a list of all keys.
    - Pop elements by index from one or multiple lists.
    - Save and load lists individually or bundled in a single `.npz` file.
    - Supports both compressed and uncompressed saving formats.
    - Handles legacy loading from old save formats.

    Methods:
    --------
    init(*keys):
        Initialize empty lists as attributes for the given keys.

    get_keys():
        Return a list of all attribute keys currently stored.

    list():
        Print all keys stored in the object.

    pop(*keys, index=0):
        Remove the element at the specified index from the specified lists
        or from all lists if no keys are provided.

    save(*keys, save_dir=''):
        Save specified lists individually as `.npz` files in the given directory.

    load(*keys, save_dir=''):
        Load specified lists individually from `.npz` files in the given directory.

    load_onefile_old(save_dir='', filename='data_record'):
        Load all lists from an old-style single `.npz` file.

    save_onefile(*keys, save_dir='', filename='data_record', compress=False):
        Save specified lists together into one `.npz` file, optionally compressed.

    load_onefile(*keys, save_dir='', filename='data_record'):
        Load specified lists from a single `.npz` file.

    Usage:
    ------
    ld = ListDict()
    ld.init('positions', 'velocities')
    ld.positions.append([1,2,3])
    ld.save_onefile('positions', 'velocities', save_dir='./data/')
    ld.load_onefile('positions', 'velocities', save_dir='./data/')
    """
    def __init__(self) -> None:
        pass

    def init(self, *keys):
        for key in keys:
            setattr(self, key, []) 
    
    def get_keys(self):
        return list(vars(self).keys())
    
    def list(self):
        print(self.get_keys())
            
    def pop(self, *keys, index=0):
        if len(keys) == 0:
            keys = self.get_keys()
        for key in keys:
            # print(key)
            getattr(self, key).pop(index)
    
    def save(self, *keys, save_dir=''):
        for key in keys:
            np.savez(save_dir + key, *getattr(self, key))
            
    def load(self, *keys, save_dir=''):
        for key in keys:
            setattr(self, key, list(np.load(save_dir + key + '.npz', allow_pickle=True).values()))
    
    def load_onefile_old(self, save_dir='', filename = 'data_record'):
        d = np.load(save_dir + filename + '.npz', allow_pickle=True)['arr_0'][()]
        for key in list(d.keys()):
            if hasattr(d[key], "__len__"):
                setattr(self, key, list(d[key]))
            else:
                setattr(self, key, d[key])
                
    def save_onefile(self, *keys, save_dir='', filename = 'data_record', compress=False):
        if len(keys) == 0:
            keys = self.get_keys()
        d = {}
        for key in keys:
            d[key] = {key: getattr(self, key)}
        if compress:
            np.savez_compressed(save_dir + filename, **d)
        else:
            np.savez(save_dir + filename, **d)
            
    def load_onefile(self, *keys, save_dir='', filename = 'data_record'):
        d = np.load(save_dir + filename + '.npz', allow_pickle=True)
        if len(keys) == 0:
            keys = list(d.keys())
        for key in keys:
            if hasattr(d[key][()][key], "__len__"):
                setattr(self, key, list(d[key][()][key]))
            else:
                setattr(self, key, d[key][()][key])
