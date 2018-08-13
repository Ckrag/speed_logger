# Speed Tester
<p>A small script that logs internet speed and outputs day-by-day logfiles, using 
<a href="https://github.com/sivel/speedtest-cli">speedtest-cli</a>.
<p>Logfiles are stored in logs/ at the root of the project. Each log contains one day, and each line is a json-string
containing information about a single log.</p>

<h3>Depedencies</h3>

```pip install -r requirements.txt```

<h3>Running</h3>
<p>Run the script</p>

```./speed_logger.py```
<p>Alternatively set an interval other than the default, as seconds

```./speed_logger.py 123```