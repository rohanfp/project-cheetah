import os

from boto3 import resource


class Signal:
    def __init__(self, signal_name):
        self.signal_name = signal_name.upper()
        self.scraper_type = None
        self.ip_address = None
        self.service_name = None
        self.timestamp = None
        self.client = resource('dynamodb', endpoint_url=os.getenv('DYNAMODB_ENDPOINT_URL'))

    def perform(self, scraper_type, ip_address, service_name=None, timestamp=None):
        self.scraper_type = scraper_type.upper()
        self.ip_address = ip_address
        self.service_name = service_name.capitalize() if service_name else None
        self.timestamp = timestamp

    def save_data(self, table_name):
        table = self.client.Table(table_name)
        item = {
            "scraper_type": self.scraper_type,
            "timestamp": self.timestamp,
            "signal_name": self.signal_name,
            "ip_address": self.ip_address,
            "service_name": self.service_name
        }
        table.put_item(Item=item)
