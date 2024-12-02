import numpy as np
from scipy.signal import lfilter, rfft, irfft


def ms(x):
    """Mean value of signal `x` squared.

    :param x: Dynamic quantity.
    :returns: Mean squared of `x`.

    """
    return (np.abs(x)**2.0).mean()



def rms(x):
    r"""Root mean squared of signal `x`.

    :param x: Dynamic quantity.

    .. math:: x_{rms} = lim_{T \\to \\infty} \\sqrt{\\frac{1}{T} \int_0^T |f(x)|^2 \\mathrm{d} t }

    :seealso: :func:`ms`.

    """
    return np.sqrt(ms(x))


def normalize(y, x=None):
    """normalize power in y to a (standard normal) white noise signal.

    Optionally normalize to power in signal `x`.

    #The mean power of a Gaussian with :math:`\\mu=0` and :math:`\\sigma=1` is 1.
    """
    #return y * np.sqrt( (np.abs(x)**2.0).mean() / (np.abs(y)**2.0).mean() )
    if x is not None:
        x = ms(x)
    else:
        x = 1.0
    return y * np.sqrt(x / ms(y))


def noise(N, color='white', state=None):
    """Noise generator.

    :param N: Amount of samples.
    :param color: Color of noise.
    :param state: State of PRNG.
    :type state: :class:`np.random.RandomState`

    """
    try:
        return _noise_generators[color](N, state)
    except KeyError:
        raise ValueError("Incorrect color.")



def white(N, state=None):
    """
    White noise.

    :param N: Amount of samples.
    :param state: State of PRNG.
    :type state: :class:`np.random.RandomState`

    White noise has a constant power density. It's narrowband spectrum is therefore flat.
    The power in white noise will increase by a factor of two for each octave band,
    and therefore increases with 3 dB per octave.
    """
    state = np.random.RandomState() if state is None else state
    return state.randn(N)


def pink(N, state=None):
    """
    Pink noise.

    :param N: Amount of samples.
    :param state: State of PRNG.
    :type state: :class:`np.random.RandomState`

    Pink noise has equal power in bands that are proportionally wide.
    Power density decreases with 3 dB per octave.

    """
    # This method uses the filter with the following coefficients.
    #b = np.array([0.049922035, -0.095993537, 0.050612699, -0.004408786])
    #a = np.array([1, -2.494956002, 2.017265875, -0.522189400])
    #return lfilter(B, A, np.random.randn(N))
    # Another way would be using the FFT
    #x = np.random.randn(N)
    #X = rfft(x) / N
    state = np.random.RandomState() if state is None else state
    uneven = N % 2
    X = state.randn(N // 2 + 1 + uneven) + 1j * state.randn(N // 2 + 1 + uneven)
    S = np.sqrt(np.arange(len(X)) + 1.)  # +1 to avoid divide by zero
    y = (irfft(X / S)).real
    if uneven:
        y = y[:-1]
    return normalize(y)

_noise_generators = {
    'white': white,
    'pink': pink
    # 'blue': blue,
    # 'brown': brown,
    # 'violet': violet,
}