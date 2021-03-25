from .signal import Signal

import os
import json


class InitSignal(Signal):
    def perform(self, ip_address, scraper_type):
        super().perform(ip_address, scraper_type)
        status_data = self.get_data()
        ip_level_status = status_data['ip_level_status']
        if scraper_type not in ip_level_status:
            ip_level_status[scraper_type] = {}
        if ip_address not in ip_level_status:
            if ip_address not in ip_level_status[scraper_type]: ip_level_status[scraper_type][ip_address] = []
        status_data['ip_level_status'] = ip_level_status
        self.save_data(status_data)
