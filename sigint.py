#!/usr/bin/env python
import signal, time

def handler(signum, time):
  print("\nI got a SIGINT, but I am not stopping")

# tell Python when SIGINT arrives, use that handler
signal.signal(signal.SIGINT, handler)

i = 0
while True:
  time.sleep(.1)
  print("\r{}".format(i), end="")
  i += 1