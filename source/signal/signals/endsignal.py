from .signal import Signal

import json

class EndSignal(Signal):
    def perform(self):
        status_data = json.load(open('../../../data/cheetah_status.json'))
        if 'scraperFeed' not in status_data[self.service_name]:
            status_data[self.service_name]['scraperFeed'] = {}
        if self.ip_address not in status_data[self.service_name]['scraperFeed']:
            status_data[self.service_name]['scraperFeed'][self.ip_address] = []
        status_data[self.service_name]['scraperFeed'][self.ip_address].append(self.timestamp)
        json.dump(status_data, open('../../../data/cheetah_status.json', 'w'))

    def log(self):
        return f"{self.signal_name}_{self.service_name}_{self.ip_address}_{self.timestamp}"
