import numpy as np
class DataProcessor():
    """
    Utility class for basic data processing tasks including range calculation,
    normalization, angle wrapping, and parameter comparisons.

    Methods:
    --------
    find_range(data):
        Computes the min and max range for 1D or 2D numpy arrays.
        For 2D data, returns arrays of min and max for each column.

    find_larger_normal_params(range1, range2):
        Compares two range arrays and returns a new range selecting the larger overlapping
        intervals based on given logic. Useful for normalizing with consistent bounds.

    data_normalize(data):
        Normalizes data to the range [0, 1] and returns normalized data and original max/min.

    runtime_normalize(data, params):
        Normalizes data using provided parameters [max, min].

    de_normalize(data, params):
        Reverts normalized data back to original scale using parameters [max, min].

    Example:
    --------
    dp = DataProcessor()
    data = np.array([[1, 2], [3, 4]])
    range_ = dp.find_range(data)
    normalized, params = dp.data_normalize(data)
    """
    def __init__(self) -> None:
        pass
    
    def find_range(self, data):
        if len(data.shape) == 1:
            return np.array([np.min(data), np.max(data)])
        range_min = []
        range_max = []
        for k in range(data.shape[1]):
            range_min.append(np.min(data[:, k]))
            range_max.append(np.max(data[:, k]))
        return np.array([range_min, range_max])

    def find_larger_normal_params(self, range1, range2):
        range_ret = range1.copy()
        for k in range(range_ret.shape[0]):
            range_ret[k, 0] = np.max([range1[k, 0], 
                                      range2[k, 0], 
                                      range1[k, 0]+range1[k, 1]-range2[k, 1],
                                      range2[k, 0]+range2[k, 1]-range1[k, 1]])
            range_ret[k, 1] = np.min([range1[k, 1], range2[k, 1]])
        return range_ret
        # for k in range(range_ret.shape[1]):
        #     range_ret[0, k] = np.min([range1[0, k], range2[0, k]])
        #     range_ret[1, k] = np.max([range1[1, k], range2[1, k]])
        # return range_ret
    
    def data_normalize(self, data):
        data_min = np.min(data)
        data = data - data_min
        data_max = np.max(data)
        data = data / data_max
        return data, [float(data_max), float(data_min)]
    
    def runtime_normalize(self, data, params):
        return (data - params[1]) / params[0]
    
    def de_normalize(self, data, params):
        return data * params[0] + params[1]