import numpy as np
import random

def gen_sine(F0, length_sec, fs=4000):
    samples = np.linspace(1, length_sec, int(fs * length_sec))
    samples = np.arange(length_sec * fs) / fs

    signal = np.sin(2 * np.pi * F0 * samples)
    return signal


def choose_freq(min=100, max=600):
    '''
    Returns the frequency of a tone, through random sampling or some other selection process to be overloaded.
    :param input: dummy variable.
    :return: frequency in hz.
    '''
    frequency_range = [min, max]
    return random.randint(frequency_range[0], frequency_range[1])



def gen_audio(length=2, fs = 16000):
    '''
    generates some tone based on some randomly chosen parameters within a constrianed set of options.
    The parameters here need to be updated. Right now, the aim is just to have some somewhat varied but simple
    sounds to be randomly generated.

    n_overtones = 0, 1, 2..7: Number of other tones above fundamental.
    harmonic = True/False: Whether the overtones are harmonically related to fundamental.
    rate = 0,1,2: A single tone, two tones in the time, or 3 tones in the time?



    :return:
    '''



    n_overtones =  random.choice([0,1,2])
    harmonic = random.choice([True, False])
    rate =  random.choice([0])

    f0 = choose_freq()


    #Generate the fundamental

    output = gen_sine(f0, length, fs)

    for n in range(0, n_overtones):
        fN = choose_freq(min=f0+10, max=2000)

        scale = np.random.rand()

        output += scale*(gen_sine(fN, length, fs))

    output = output/(np.max(np.abs(output)))
    return output

