import numpy as np
import linecache

class Array_mat_utils(object):
    def __init__(self):
        self.a = 1

    # 完成两个tensor的按行拼接
    def two_vec_splic(self, tensor1, tensor2):
        return np.vstack((tensor1, tensor2))

    def two_vec_hsplic(self,tensor1, tensor2):
        return np.hstack((tensor1,tensor2))

if __name__ == '__main__':
    array_mat = Array_mat_utils()
    arr1 = np.array([1,2,3,5])
    arr2 = np.array([4,5,6])
    arr3 = np.hstack((arr1, arr2))
    print(np.hstack((arr1, arr3)))