def mse(n,target:list,actual:list):
    return (1/n)*(sum([(actual[i]-target[i])**2 for i in range(len(target))]))


import numpy as np

def mse_numpy(target, actual):
    target = np.array(target)
    actual = np.array(actual)
    return np.mean((actual - target) ** 2)

def mae(target:list,actual:list):
    n=len(target)
    return (1/n)*(sum([abs(actual[i]-target[i]) for i in range(len(target))]))
