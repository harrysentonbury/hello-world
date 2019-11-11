
import argparse
import numpy as np
import sounddevice as sd
import time


def play(frequency=440, duration=1.5):
    sample_rate = 44100

    x = np.linspace(0, duration, duration * sample_rate)
    wave = np.sin(2 * np.pi * x * frequency) * 0.3

    sd.play(wave, sample_rate)
    time.sleep(duration)
    sd.stop()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("frequency", help="The required frequency in hertz", type=float)
    parser.add_argument("duration", nargs='?',
                        help="Required duration in seconds", type=float)
    args = parser.parse_args()

    try:
        if args.duration:
            play(args.frequency, args.duration)
        else:
            play(args.frequency)
    except ValueError:
        return play(args.frequency)


if __name__ == '__main__':
    main()
