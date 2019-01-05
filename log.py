import json
import os.path
import subprocess
import time
import traceback

import requests
from time import sleep

class Log:

    def __init__(self):
        self._LOG_FOLDER_PATH = "logs"
        self._BAD_LOG_ENTRY_TEXT = "bad log entry"
        self._DAY_STAMP_FORMAT = "%Y-%m-%d"
        self._TIME_STAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
        self._NO_CONNECTION_ERROR = "Name or service not known"

        self._external_cache = []

    def _write_to_log(self, file, txt_to_log):
        with open(file, "a+") as f:
            f.write(txt_to_log)

    def _get_log_path(self, name):
        filename = self._LOG_FOLDER_PATH + "/" + name
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        return filename

    def _get_log_name(self):
        return self._get_day_timestamp()

    def _get_day_timestamp(self):
        return time.strftime(self._DAY_STAMP_FORMAT)

    def _get_timestamp(self):
        return time.strftime(self._TIME_STAMP_FORMAT)

    def _make_log_entry(self):
        stdoutdata = subprocess.getoutput("speedtest-cli --json")

        json_data = self._BAD_LOG_ENTRY_TEXT
        try:
            json_data = json.loads(stdoutdata)
            json_data = stdoutdata  # Eeeeh, we just need the json string, but atleast this validates :D
        except Exception as e:
            if self._NO_CONNECTION_ERROR in stdoutdata:
                print("No connection: {}".format(stdoutdata))
            else:
                print("Exception: {}".format(e))
                print(traceback.format_exc())

        return json_data

    def log(self, entry_delimiter="\n", dms=None):
        if not dms:
            self._log_local(entry_delimiter)
        else:
            self._log_post(dms)

    def _log_local(self, entry_delimiter):
        text = self._make_log_entry() + entry_delimiter
        file_name = self._get_log_name()
        file = self._get_log_path(file_name)
        self._write_to_log(file, text)

    def _log_post(self, url):
        try:
            self._external_cache.append(self._make_log_entry())

            while self._external_cache:
                text = self._external_cache[0]

                resp = requests.post("{}/app/{}".format(url, "home_internet"), data=text, auth=('admin', 'Secret123'))
                if resp.status_code is 200:
                    self._external_cache.pop(0)
        except:
            sleep(5)
