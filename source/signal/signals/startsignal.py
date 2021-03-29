from .signal import Signal

import os
import json


class StartSignal(Signal):
    def perform(self, scraper_type, ip_address, service_name, timestamp):
        super().perform(scraper_type, ip_address, service_name, timestamp)
        table_name = 'ip-level-status'
        filter_conditions = {
            'scraper_type': self.scraper_type,
            'ip_address': self.ip_address
        }
        status_data = self.get_data(table_name, filter_conditions)
        status_data = status_data[0]
        status_data['to_restrict_list'].append(self.service_name)
        self.save_data(table_name, status_data)
        table_name = 'service-level-status'
        filter_conditions = {
            'scraper_type': self.scraper_type,
            'service_name': self.service_name
        }
        status_data = self.get_data(table_name, filter_conditions)
        status_data = [item for item in status_data if item['ip_address'] == self.ip_address]
        if not status_data:
            status_data = {
                'scraper_type': self.scraper_type,
                'service_name': self.service_name,
                'ip_address': self.ip_address,
                'latest_start_timestamp': self.timestamp,
                'latest_end_timestamp': None,
                'average_execution_time': 0,
                'execution_count': 1
            }
        else:
            status_data = status_data[0]
            status_data['latest_start_timestamp'] = self.timestamp
        self.save_data(table_name, status_data)
