import time
import json
from random import random, randint, choices
from scraper import Scraper


def read_file(file_path):
    # Read and return data
    file_data = json.load(open(file_path, 'r'))
    return file_data


def write_file(data, file_name):
    # Write data
    json.dump(data, open(file_name, 'w'), indent=4)


def record_ip_address(competitor_name, ip_address, file_path):
    status_data = read_file(file_path)

    # Record IPs available
    if competitor_name not in status_data: status_data[competitor_name] = {}
    if "queue" not in status_data[competitor_name]: status_data[competitor_name]["queue"] = []
    for competitor_name in status_data:
        if ip_address not in status_data[competitor_name]["queue"]: status_data[competitor_name]["queue"].append(ip_address)
        print(competitor_name, status_data[competitor_name]["queue"])
    write_file(status_data, file_path)


def set_ip_address_priority(competitor_name, ip_address, operation_duration, file_path):
    status_data = read_file(file_path)

    # Record IPs competitor wise
    if competitor_name not in status_data: status_data[competitor_name] = {}
    if "queueWeights" not in status_data[competitor_name]: status_data[competitor_name]["queueWeights"] = {}
    if ip_address not in status_data[competitor_name]["queueWeights"]: status_data[competitor_name]["queueWeights"][ip_address] = 1

    write_file(status_data, file_path)


def update_ip_address_execution(competitor_name, ip_address, timestamp, file_path):
    status_data = read_file(file_path)
    
    # Record execution timestamps IP wise
    if competitor_name not in status_data: status_data[competitor_name] = {}
    if "scraperFeed" not in status_data[competitor_name]: status_data[competitor_name]["scraperFeed"] = {}
    if ip_address not in status_data[competitor_name]["scraperFeed"]: status_data[competitor_name]["scraperFeed"][ip_address] = []
    status_data[competitor_name]["scraperFeed"][ip_address].append(timestamp)
    
    write_file(status_data, file_path)


def get_recommended_ip_address(competitor_name, file_path):
    status_data = read_file(file_path)

    # Get available IP list and utilized IP list
    if competitor_name in status_data and "queue" in status_data[competitor_name]:
        recommended_ip_address = status_data[competitor_name]["queue"].pop(0)
        status_data[competitor_name]["queue"].append(recommended_ip_address)
    else:
        recommended_ip_address = None
    
    write_file(status_data, file_path)
    return competitor_name, recommended_ip_address


def cheetah(competitor_name, ip_address, operation, operation_duration, timestamp, file_path):
    recommended_ip_address = None
    if operation == "START":
        record_ip_address(competitor_name, ip_address, file_path)
    elif operation == "REQUEST":
        set_ip_address_priority(competitor_name, ip_address, operation_duration, file_path)
    elif operation == "STOP":
        update_ip_address_execution(competitor_name, ip_address, timestamp, file_path)
        competitor_name, recommended_ip_address = get_recommended_ip_address(competitor_name, file_path)
    return competitor_name, recommended_ip_address
