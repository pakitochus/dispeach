from scipy.signal import butter, lfilter
import numpy as np 

# low-pass filter
def low_pass_filter(audio: np.ndarray, cutoff: float, order: int = 5, Fs: int = 16000) -> np.ndarray:
    nyq = 0.5 * Fs
    low = cutoff / nyq
    b, a = butter(order, [low], btype='low')
    return lfilter(b, a, audio)