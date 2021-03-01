import sys
import time
from random import choices
from scraper import Lambda, Scraper
from cheetah import *


def record_scraper_status(competitor_name, ip_address, timestamp, operation, file_path):
    status_data = read_file(file_path)
    status_data.append(f"{competitor_name}_{ip_address}_{operation}_{timestamp}")
    write_file(status_data, file_path)


def get_scraper_status(competitor_names, lambda_instances, operations, status=[]):
    ip_address = choices(lambda_instances)[0]
    competitor_name = choices(competitor_names)[0]
    if f"{competitor_name}_{ip_address}" not in status:
        status.append(f"{competitor_name}_{ip_address}")
        operation = "START"
    else:
        operation = choices(operations, [1, 100])[0]
        if operation == "START":
            status.append(f"{competitor_name}_{ip_address}")
        elif operation == "STOP":
            status.remove(f"{competitor_name}_{ip_address}")
    return competitor_name, ip_address, operation, status


if __name__ == "__main__":
    file_path = f'./data/scraper_status.json'
    competitor_names = ['Grab', 'Deliveroo', 'Uber', 'Google', 'Gofood']
    iterations = int(sys.argv[1])
    lambda_instances = [Lambda() for i in range(10)]
    operations = ["START", "STOP"]
    timestamp = time.time()
    status = []

    write_file([], file_path)
    
    # Generate status file
    for i in range(iterations):
        print(f"Start of iteration {i+1}")
        competitor_name, ip_address, operation, status = get_scraper_status(
            competitor_names,
            lambda_instances,
            operations,
            status
        )
        timestamp += choices([1,2,3,4,5])[0]
        record_scraper_status(competitor_name, ip_address, timestamp, operation, file_path)
        print(f"Competitor name - {competitor_name}, Execution IP - {ip_address}, Timestamp - {timestamp}")
        print(f"End of iteration {i+1}\n")
