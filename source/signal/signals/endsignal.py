from .signal import Signal
# from ...recommendation import Engine

import os
import json


class EndSignal(Signal):
    def perform(self, ip_address, scraper_type, service_name, timestamp):
        super().perform(ip_address, scraper_type, service_name, timestamp)
        status_data = self.get_data()
        service_level_status = status_data['service_level_status']
        service_level_status[self.scraper_type][self.service_name][self.ip_address]['end_timestamp'] = self.timestamp
        service_level_status[self.scraper_type][self.service_name][self.ip_address]['scrape_time_average'] = 0
        service_level_status[self.scraper_type][self.service_name][self.ip_address]['execution_count'] += 1
        status_data['service_level_status'] = service_level_status
        self.save_data(status_data)

