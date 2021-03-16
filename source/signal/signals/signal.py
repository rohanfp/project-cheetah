import time
from dotenv import load_dotenv


class Signal:
    def __init__(self, signal_name, service_name, ip_address):
        self.signal_name = signal_name.upper()
        self.service_name = service_name.lower()
        self.ip_address = ip_address
        self.timestamp = time.time()
        load_dotenv(dotenv_path='../../.env')

    def perform(self):
        pass

    def log(self):
        pass
