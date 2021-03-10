import sys
import json
from cheetah import *


if __name__ == "__main__":
    scraper_status = json.load(open(sys.argv[1], 'r'))
    iterations = len(scraper_status)
    cheetah_output = []

    # Cleanup cheetah status file
    write_file({}, sys.argv[2])

    # Start driver program
    for i in range(iterations):
        print(f"Start of iteration {i+1}")
        competitor_name, ip_address, operation, operation_duration, timestamp = scraper_status[i].split(',')
        competitor_name, recommended_ip_address = cheetah(competitor_name, ip_address, operation, operation_duration, timestamp, sys.argv[2])
        if operation == "STOP": cheetah_output.append(f"{competitor_name},{recommended_ip_address}")
        print(f"Competitor name - {competitor_name}, Execution IP - {ip_address} operation - {operation} Recommended IP - {recommended_ip_address}")
        print(f"End of iteration {i+1}\n")

    write_file(cheetah_output, "data/cheetah_output.json")