import numpy as np 

class kEvenDistortion:
    """
    k-even distortion.

    from https://www.musicdsp.org/en/latest/Effects/43-waveshaper.html?highlight=odd%20harmonics

    (input: a == "overdrive amount")

    z = M_PI * a;
    s = 1/sin(z)
    b = 1/a

    if (x > b)
      f(x) = 1
    else
      f(x) = sin(z*x)*s
    """
    def __init__(self, a: float):
        self.a = a

    def distort(self, audio: np.ndarray) -> np.ndarray:
        z = np.pi * self.a
        s = 1 / np.sin(z)
        b = 1 / self.a

        audio_distorted = np.zeros_like(audio)
        audio_distorted[audio > b] = 1
        audio_distorted[audio <= b] = np.sin(z * audio[audio <= b]) * s

        return audio_distorted
