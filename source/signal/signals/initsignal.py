from .signal import Signal

import os
import json


class InitSignal(Signal):
    def perform(self):
        status_data = json.load(open(os.getenv('DATABASE'), 'r'))
        if self.service_name not in status_data:
            status_data[self.service_name] = {}
        if 'queue' not in status_data[self.service_name]:
            status_data[self.service_name]['queue'] = []
        if 'queueWeights' not in status_data[self.service_name]:
            status_data[self.service_name]['queueWeights'] = {}
        if 'scraperFeed' not in status_data[self.service_name]:
            status_data[self.service_name]['scraperFeed'] = {}
            status_data[self.service_name]['scraperFeed'][self.ip_address] = {
                'startTime': None,
                'endTime': None,
                'count': None,
            }
        for service_name in status_data:
            if self.ip_address not in status_data[service_name]['queue']:
                status_data[service_name]['queue'].append(self.ip_address)
        status_data[self.service_name]['queueWeights'][self.ip_address] = 1
        json.dump(status_data, open(os.getenv('DATABASE'), 'w'), indent=4)
        return {'code': 200, 'data': None}

    def log(self):
        return f"{self.signal_name}_{self.service_name}_{self.ip_address}_{self.timestamp}"
