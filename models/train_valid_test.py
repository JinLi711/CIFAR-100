import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import sys
sys.path.insert(0, '../')
import get_data

train = get_data.unpickle('../data/train')
meta = get_data.unpickle('../data/meta')
test = get_data.unpickle('../data/test')

# map number assignment (position in the list) to label
# "fine" label  : the class to which it belongs
# "coarse" label: the superclass to which it belongs

fine_labels = get_data.decode_list(meta, b'fine_label_names')
coarse_labels = get_data.decode_list(meta, b'coarse_label_names')

def train_validate_test (train, test, valid_size=.2):
    
    """
    :param train: a dictionary of the train set items 
    :type  train: dict
    :param test: a dictionary of the test set items
    :type  test: dict
    :param valid_size: The proportion of the validation set in decimal
    :type  valid_size: float
    :return: Train, validation, and test set for image, class, and superclass
    :rtype:  (numpy.ndarray, numpy.ndarray, numpy.ndarray, 
              numpy.ndarray, numpy.ndarray, numpy.ndarray, 
              numpy.ndarray, numpy.ndarray, numpy.ndarray)
    """
    
    
    X = train[b'data'] / 255 # constant scale
    X = X.reshape([-1,3,32,32]).transpose([0,2,3,1]) 
    fine_y = train[b'fine_labels']
    coarse_y = train[b'coarse_labels']
    
    valid_index = round (X.shape[0] * valid_size)
    valid_X, train_X = X[:valid_index], X[valid_index:]
    
    valid_fine_y, train_fine_y = fine_y[:valid_index], fine_y[valid_index:]
    valid_coarse_y, train_coarse_y = coarse_y[:valid_index], coarse_y[valid_index:]
    
    test_X = test[b'data'] / 255
    test_X = test_X.reshape([-1,3,32,32]).transpose([0,2,3,1])
    test_fine_y = test[b'fine_labels']
    test_coarse_y = test[b'coarse_labels']
    
    # change to one-hot
    from keras.utils import to_categorical
    valid_fine_y   = to_categorical (valid_fine_y)
    valid_coarse_y = to_categorical (valid_coarse_y)
    train_fine_y   = to_categorical (train_fine_y)
    train_coarse_y = to_categorical (train_coarse_y)
    test_fine_y    = to_categorical (test_fine_y)
    test_coarse_y  = to_categorical (test_coarse_y)
    
    print ('Size of Train Set is: {}'.format(train_X.shape[0]) )
    print ('Size of Validation Set is: {}'.format(valid_X.shape[0]) )
    print ('Size of Test Set is: {}'.format(test_X.shape[0]) )
    
    return (train_X, train_fine_y, train_coarse_y,
            valid_X, valid_fine_y, valid_coarse_y,
            test_X, test_fine_y, test_coarse_y)

(train_X, train_fine_y, train_coarse_y,
valid_X, valid_fine_y, valid_coarse_y,
test_X, test_fine_y, test_coarse_y) = train_validate_test (train, test, valid_size=.2)