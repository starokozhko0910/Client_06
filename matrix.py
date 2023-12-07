import numpy as np
import sys
class Matrix:
    def __init__(self, min, max):
        assert min>0, "Min should be equal or greater that zero"
        assert max>1, "Max should equal or great than one"
        assert max>=min, "Min should be less than Max"

        self._M = np.random.randint(min, max)
        self._N = np.random.randint(min, max)
        self._L = np.random.randint(min, max)

    def create_matrix(self):
        first_matrix = np.random.uniform(low =  1000, high = 100000, size = (self._N, self._M))
        second_matrix = np.random.uniform(low = 1000, high = 100000,  size = (self._M, self._L))
        return first_matrix, second_matrix
