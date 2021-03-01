import time
from random import random, randint, choices


class Lambda:
    # Mocking AWS lambda
    def __init__(self, ip_address=None):
        if ip_address:
            self.ip_address = ip_address
        else:
            self.ip_address = self.generate_random_ip()
        self.created_on = int(time.time())

    def __str__(self):
        return self.ip_address

    def generate_random_ip(self):
        return f'{randint(0, 256)}.{randint(0, 256)}.{randint(0, 256)}.{randint(0, 256)}'

    def generate_random_lambda_execution_time(self):
        return random()

    def execute_lambda(self, competitor_name, to_sleep=True):
        execution_time = self.generate_random_lambda_execution_time()
        if to_sleep:
            time.sleep(execution_time)
        return self.ip_address, competitor_name, execution_time


class Scraper:
    # Mocking a scraper on AWS lambda

    def __init__(self, lambda_instances):
        self.lambda_instances = lambda_instances
        self.lambda_instance_count = None

    def create_lambda_instances(self, lambda_instance_count=10):
        lambda_instances = {}
        for i in range(lambda_instance_count):
            lambda_instance = Lambda()
            lambda_instances[lambda_instance.__str__()] = lambda_instance
        return lambda_instances

    def execute_scraper_lambda(self, avoidable_ip_address_list=None, competitor_name=None, to_sleep=True):
        # Execute scraping on random ip if not provided as an argument
        if avoidable_ip_address_list:
            recommended_ip_address_list = list(set(self.lambda_instances).difference(set(avoidable_ip_address_list)))
        else:
            recommended_ip_address_list = list(self.lambda_instances)
        if recommended_ip_address_list:
            ip_address = choices(recommended_ip_address_list)[0]
            ip_address, competitor_name, execution_time = self.lambda_instances[ip_address].execute_lambda(competitor_name, to_sleep)
        else:
            ip_address = None
            execution_time = None
        return ip_address, competitor_name, execution_time
