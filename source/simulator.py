import sys
import json
from scraper import Scraper, Lambda
from cheetah import *


if __name__ == "__main__":
    scraper_status = json.load(open(sys.argv[1], 'r'))
    iterations = len(scraper_status)
    lambda_instances = {}
    scraper = Scraper({})
    toggle = sys.argv[3]

    # Cleanup cheetah status file
    write_file({}, sys.argv[2])

    # Start driver program
    for i in range(iterations):
        print(f"Start of iteration {i+1}")
        competitor_name, ip_address, operation, timestamp = scraper_status[i].split('_')
        if operation == "STOP":
            record_ip_status(ip_address, competitor_name, timestamp, sys.argv[2])
        if ip_address in scraper.lambda_instances:
            lambda_instance = scraper.lambda_instances[lambda_instance.__str__()]
        else:
            lambda_instance = Lambda(ip_address)
            scraper.lambda_instances[lambda_instance.__str__()] = lambda_instance
        if sys.argv[3] == "ON":
            avoidable_ip_address_list = cheetah(competitor_name, sys.argv[2])
            ip_address, competitor_name, execution_time = scraper.execute_scraper_lambda(
                avoidable_ip_address_list=avoidable_ip_address_list,
                competitor_name=competitor_name,
                to_sleep=False
            )
            if ip_address and execution_time:
                record_ip_status(ip_address, competitor_name, timestamp, sys.argv[2])
        else:
            avoidable_ip_address_list = []
        print(f"Competitor name - {competitor_name}, Avoidable IP list - {avoidable_ip_address_list}, Execution IP - {ip_address}, Execution Time - {timestamp}")
        print(f"End of iteration {i+1}\n")
