from .signal import Signal

import os
import json


class StartSignal(Signal):
    def perform(self, ip_address, scraper_type, service_name, timestamp):
        super().perform(ip_address, scraper_type, service_name, timestamp)
        status_data = self.get_data()
        service_level_status = status_data['service_level_status']
        if self.scraper_type not in service_level_status:
            service_level_status[self.scraper_type] = {}
        if self.service_name not in service_level_status[self.scraper_type]:
            service_level_status[self.scraper_type][self.service_name] = {}
        if self.ip_address not in service_level_status[self.scraper_type][self.service_name]:
            service_level_status[self.scraper_type][self.service_name][self.ip_address] = {
                'start_timestamp': self.timestamp,
                'end_timestamp': None,
                'scrape_time_average': 0,
                'execution_count': 0
            }
        service_level_status[self.scraper_type][self.service_name][self.ip_address]['start_timestamp'] = self.timestamp
        service_level_status[self.scraper_type][self.service_name][self.ip_address]['end_timestamp'] = None
        status_data['service_level_status'] = service_level_status
        self.save_data(status_data)
