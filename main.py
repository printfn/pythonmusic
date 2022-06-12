#!/usr/bin/env python3

from pysinewave import SineWave
import time

def play_freq(freq, sleep_duration):
	sinewave = SineWave(pitch_per_second=10000)
	sinewave.set_frequency(freq)
	sinewave.play()
	time.sleep(sleep_duration)
	sinewave.stop()

def play_subdivisions(divs, sleep_duration, indices=None):
	if indices is None:
		indices = range(divs + 1)
	for i in indices:
		play_freq(220 * 2 ** (i/divs), sleep_duration)

# semitones
play_subdivisions(12, 0.25)

# major scale
play_subdivisions(12, 0.25, indices=[0, 2, 4, 5, 7, 9, 11, 12])

# harmonic minor
play_subdivisions(12, 0.25, indices=[0, 2, 3, 5, 7, 8, 11, 12])

# melodic minor
play_subdivisions(12, 0.25, indices=[0, 2, 3, 5, 7, 9, 11, 12, 10, 8, 7, 5, 3, 2, 0])
