from .signal import Signal
# from ...recommendation import Engine

import os
from decimal import Decimal


class EndSignal(Signal):
    def perform(self, scraper_type, ip_address, service_name, timestamp):
        super().perform(scraper_type, ip_address, service_name, timestamp)
        ip_level_table_name = 'ip-level-status'
        service_level_table_name = 'service-level-status'
        filter_conditions = {
            'scraper_type': self.scraper_type,
            'service_name': self.service_name
        }
        service_level_status_data = self.get_data(service_level_table_name, filter_conditions)
        for item in service_level_status_data:
            if float(self.timestamp) - float(item['latest_start_timestamp']) > 300:
                filter_conditions = {
                    'scraper_type': self.scraper_type,
                    'ip_address': item['ip_address']
                }
                to_restrict_list = self.get_data(ip_level_table_name, filter_conditions)['to_restrict_list']
                to_restrict_list.remove(self.service_name)
                ip_level_status_data = {
                    'scraper_type': self.scraper_type,
                    'ip_address': self.ip_address,
                    'to_restrict_list': to_restrict_list
                }
                self.save_data(ip_level_table_name, ip_level_status_data)
            if item['ip_address'] == self.ip_address:
                item['latest_end_timestamp'] = self.timestamp
                execution_time = float(item['latest_end_timestamp']) - float(item['latest_start_timestamp'])
                execution_count = int(item['execution_count'])
                average_execution_time = float(item['average_execution_time'])
                item['average_execution_time'] = Decimal((execution_time + (average_execution_time * execution_count))/(execution_count + 1))
                item['execution_count'] += 1
                self.save_data(service_level_table_name, item)
        recommended_ip_address = None
        return recommended_ip_address
