import numpy as np
from scipy import stats

def npprint_suppress():
    np.set_printoptions(suppress=True, precision=10)
    
def modified_sigmoid(x, steepness, where_fn_is_05):
    return 1 / (1 + np.exp(-steepness * (x - where_fn_is_05)))

def truncated_normal_sampler(mean, std, lower_bound, upper_bound, size=1):
    if std == 0:
        return np.ones(size) * mean
    a, b = (lower_bound - mean) / std, (upper_bound - mean) / std
    return stats.truncnorm.rvs(a, b, loc=mean, scale=std, size=size)    

def get_subsample_inds(length, subsample_num=None):
    if subsample_num is None:
        return np.arange(length)
    if subsample_num > length:
        subsample_num = length
    return np.random.permutation(length)[:subsample_num]

def readTXT(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines