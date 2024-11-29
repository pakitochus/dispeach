import numpy as np 

class kEvenDistortion:
    def __init__(self, k: int):
        self.k = k

    def distort(self, audio: np.ndarray) -> np.ndarray:
        return audio