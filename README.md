# internet_monitoring
Scripts you can use to track your internet latency, outages and internet speed.

In order to use to tools, you must have `python` interpreter installed. Then, make sure that you run the scripts with root (administrator) permissions.

Both tools will log their tests into `.csv` format.

To customize which servers will the `ping.py` script ping, you can add an entry in the `servers` list. 
You can also customize how often will the scripts run. The default is speedtest every 60 seconds, and a ping test every 10 seconds.

Just note that the scripts are using [this](https://github.com/sivel/speedtest-cli) speedtest library, and [this](https://pypi.org/project/pythonping/) ICMP pinging library.
