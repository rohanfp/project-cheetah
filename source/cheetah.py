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


def record_ip_status(ip_address, competitor_name, timestamp=time.time(), file_path='../data/status.json'):
    status_data = read_file(file_path)

    # Record IPs available
    if "IP" not in status_data:
        status_data["IP"] = []

    status_data["IP"].append(ip_address)
    status_data["IP"] = list(set(status_data["IP"]))
    
    # Record IPs competitor wise
    if competitor_name not in status_data:
        status_data[competitor_name] = {}
    
    # Record execution timestamps IP wise
    if ip_address not in status_data[competitor_name]:
        status_data[competitor_name][ip_address] = []

    status_data[competitor_name][ip_address].append(timestamp)
    write_file(status_data, file_path)


def get_avoidable_ip_address_using_status(competitor_name, file_path):
    status_data = read_file(file_path)

    # Get available IP list and utilized IP list
    if 'IP' in status_data and competitor_name in status_data:
        if len(status_data['IP']) > len(list(status_data[competitor_name])):
            avoidable_ip_address_list = list(status_data[competitor_name])
        else:
            avoidable_ip_address_list = list(status_data[competitor_name])
            for ip_address in avoidable_ip_address_list:
                if time.time() - float(max(status_data[competitor_name][ip_address])) >= 5:
                    avoidable_ip_address_list.remove(ip_address)
    else:
        avoidable_ip_address_list = []
    return avoidable_ip_address_list


def cheetah(competitor_name, file_path):
    avoidable_ip_address_list = get_avoidable_ip_address_using_status(competitor_name, file_path)
    return avoidable_ip_address_list
