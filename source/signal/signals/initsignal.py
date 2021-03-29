from .signal import Signal

import os
import json


class InitSignal(Signal):
    def perform(self, scraper_type, ip_address):
        super().perform(scraper_type, ip_address)
        status_data = {
            'scraper_type': self.scraper_type,
            'ip_address': self.ip_address,
            'to_restrict_list': []
        }
        table_name = 'ip-level-status'
        self.save_data(table_name, status_data)
