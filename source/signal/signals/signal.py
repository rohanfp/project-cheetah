import time
import os
import json


class Signal:
    def __init__(self, signal_name):
        self.signal_name = signal_name.upper()
        self.scraper_type = None
        self.ip_address = None
        self.service_name = None
        self.timestamp = None

    def perform(self, ip_address, scraper_type, service_name=None, timestamp=None):
        self.ip_address = ip_address
        self.scraper_type = scraper_type.upper()
        self.service_name = service_name.lower() if service_name else None
        self.timestamp = timestamp

    def get_data(self):
        status_data = json.load(open(os.getenv('DATABASE'), 'r'))
        return status_data

    def save_data(self, status_data):
        json.dump(status_data, open(os.getenv('DATABASE'), 'w'), indent=4)
