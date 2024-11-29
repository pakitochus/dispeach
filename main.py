import numpy as np 
import sys
import scipy as sp 
from dispeach.distortion import kEvenDistortion


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_path>")
        sys.exit(1)

    audio_path = sys.argv[1]

    # load audio file
    audio, sr = sp.io.wavfile.read(audio_path)

