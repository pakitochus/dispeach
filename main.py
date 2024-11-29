import numpy as np 
import sys
import scipy as sp 
import os
from dispeach.distortion import kEvenDistortion
from dispeach.filtering import low_pass_filter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_path>")
        sys.exit(1)

    audio_path = sys.argv[1]

    # load audio file
    sr, audio = sp.io.wavfile.read(audio_path)

    # low-pass filter
    audio_lp = low_pass_filter(audio, 1000, 5, sr)

    # save filtered audio
    sp.io.wavfile.write(os.path.join('output', 'filtered_audio.wav'), sr, audio_lp)
