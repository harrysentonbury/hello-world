#!/usr/bin/env python3

import argparse
import numpy as np
import sounddevice as sd
import time


def play(frequency=440, duration=1.5):
    sample_rate = 48000
    if frequency <= 0:
        print('must be positive numbers')
        parser.print_help()
    if duration <= 0:
        print('must be positive numbers')
        parser.print_help()
    else:
        x = np.linspace(0, duration, int(duration * sample_rate))
        wave = np.sin(2 * np.pi * x * frequency) * 0.3

        sd.play(wave, sample_rate)
        time.sleep(duration)
        sd.stop()


parser = argparse.ArgumentParser()
parser.add_argument(
    "frequency", nargs='?', help="required frequency in hertz", type=float)
parser.add_argument("duration", nargs="?",
                    help="required duration in seconds", type=float)
args = parser.parse_args()

try:
    if args.duration:
        play(args.frequency, args.duration)
    elif args.frequency:
        play(args.frequency)
    else:
        play()
except ValueError:
    play(args.frequency)
except KeyboardInterrupt:
    parser.exit("\n Interupt by user")
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
