#!/usr/bin/python3

import log
import time

_LOG_INTERVAL_SEC = 60

# Run
log = log.Log()

print("Logging started")

while True:
    log.log()
    time.sleep(_LOG_INTERVAL_SEC)