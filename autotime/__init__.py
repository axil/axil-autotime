from __future__ import print_function

import time
import sys
import re

__version__ = '0.3'

from time import strftime, localtime

from IPython.core.magics.execution import _format_time as format_delta

if sys.version_info >= (3, 3):
    _timer = time.perf_counter
elif sys.platform == 'win32':
    _timer = time.clock
else:
    _timer = time.time


def format_timestamp(struct_time):
    timestamp = strftime('%Y-%m-%d %H:%M:%S %z', struct_time)
    # add colon in %z (for datetime.fromisoformat, stackoverflow.com/q/44836581)
    return '{}:{}'.format(timestamp[:-2], timestamp[-2:])


class LineWatcher(object):
    """Class that implements a basic timer.

    Notes
    -----
    * Register the `start` and `stop` methods with the IPython events API.
    """
    __slots__ = ['start_time', 'timestamp']

    def start(self, *args, **kwargs):
        self.start_time = _timer()

    def stop(self, result):
        stop_time = _timer()
        raw = result.info.raw_cell
        defs_only = all(re.match('def|class|\s', line) for line in raw.split('\n'))

        if not defs_only and self.start_time:
            diff = stop_time - self.start_time
            assert diff >= 0
            print('elapsed: {}'.format(format_delta(diff)))


timer = LineWatcher()
start = timer.start
stop = timer.stop


def load_ipython_extension(ip):
    start()
    ip.events.register('pre_run_cell', start)
    ip.events.register('post_run_cell', stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', start)
    ip.events.unregister('post_run_cell', stop)

