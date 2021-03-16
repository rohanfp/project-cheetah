from .signal import Signal

import os
import json


class StartSignal(Signal):
    def perform(self):
        status_data = json.load(open(os.getenv('DATABASE'), 'r'))
        status_data[self.service_name]['scraperFeed'][self.ip_address]['startTime'] = self.timestamp
        json.dump(status_data, open(os.getenv('DATABASE'), 'w'), indent=4)

    def log(self):
        return f"{self.signal_name}_{self.service_name}_{self.ip_address}_{self.timestamp}"
