import sys
import time
from random import choices, random, randint
from scraper import Lambda, Scraper
from cheetah import *


def generate_random_ip():
    return f'{randint(0, 256)}.{randint(0, 256)}.{randint(0, 256)}.{randint(0, 256)}'


def record_scraper_status(competitor_name, ip_address, timestamp, operation, file_path):
    status_data = read_file(file_path)
    if operation == "REQUEST":
        operation_duration = random() + randint(0,1)
    else:
        operation_duration = ""
    status_data.append(f"{competitor_name},{ip_address},{operation},{operation_duration},{timestamp}")
    write_file(status_data, file_path)


def get_scraper_status(competitor_names, lambda_instances, operations, status=[]):
    ip_address = choices(lambda_instances)[0]
    competitor_name = choices(competitor_names)[0]
    if f"{competitor_name},{ip_address},START" in status and f"{competitor_name},{ip_address},REQUEST" in status:
        status.remove(f"{competitor_name},{ip_address},START")
        status.remove(f"{competitor_name},{ip_address},REQUEST")
        competitor_names.remove(competitor_name)
        operation = "STOP"
    elif f"{competitor_name},{ip_address},START" in status:
        status.append(f"{competitor_name},{ip_address},REQUEST")
        operation = "REQUEST"
    else:
        status.append(f"{competitor_name},{ip_address},START")
        competitor_names.append(competitor_name)
        operation = "START"
    return competitor_name, ip_address, operation, status


if __name__ == "__main__":
    file_path = sys.argv[1]
    competitor_names = ['Grab', 'Deliveroo', 'Uber', 'Google', 'Gofood']
    iterations = int(sys.argv[2])
    lambda_instances = [generate_random_ip() for i in range(10)]
    operations = ["START", "REQUEST", "STOP"]
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
        timestamp += choices([1,2,3])[0] + random()
        record_scraper_status(competitor_name, ip_address, timestamp, operation, file_path)
        print(f"Competitor name - {competitor_name}, Execution IP - {ip_address}, Timestamp - {timestamp}")
        print(f"End of iteration {i+1}\n")
