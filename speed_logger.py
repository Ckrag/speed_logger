#!/usr/bin/python3

import log
import time
import sys

_LOG_INTERVAL_SEC = 60

# Run
if len(sys.argv) > 1:
    _LOG_INTERVAL_SEC = int(sys.argv[1])

log = log.Log()

print("Logging started")
print("Log interval: {}".format(_LOG_INTERVAL_SEC))

while True:
    print(str(log._get_timestamp()) + " - testing ..")
    log.log()
    time.sleep(_LOG_INTERVAL_SEC)