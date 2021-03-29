import os

from boto3 import resource
from boto3.dynamodb.conditions import Key, And
from functools import reduce


class Signal:
    def __init__(self, signal_name):
        self.signal_name = signal_name.upper()
        self.scraper_type = None
        self.ip_address = None
        self.service_name = None
        self.timestamp = None
        self.client = resource('dynamodb', endpoint_url=os.getenv('DYNAMODB_ENDPOINT_URL'))

    def perform(self, scraper_type, ip_address, service_name=None, timestamp=None):
        self.ip_address = ip_address
        self.scraper_type = scraper_type.upper()
        self.service_name = service_name.lower() if service_name else None
        self.timestamp = timestamp

    def get_data(self, table_name, filter_conditions):
        table = self.client.Table(table_name)
        status_data = table.query(
            KeyConditionExpression=reduce(And, ([Key(key).eq(value) for key, value in filter_conditions.items()]))
        )['Items']
        return status_data

    def save_data(self, table_name, status_data):
        table = self.client.Table(table_name)
        table.put_item(Item=status_data)
