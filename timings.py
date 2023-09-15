import time
import sys

def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def rest(x):
    time.sleep(x * 0.5)
