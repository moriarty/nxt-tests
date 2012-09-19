#!/usr/bin/env python

import nxt.locator
import nxt.sensor as sensor
import time

def play_beep(b):
    b.play_tone(200,200)

if __name__ == '__main__':
    b = nxt.locator.find_one_brick()
    play_beep(b)
    exit()
