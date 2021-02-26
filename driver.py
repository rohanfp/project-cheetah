import sys
from source.scraper import Scraper
from source.cheetah import *


if __name__ == "__main__":
    file_path = './data/status.json'
    scraper = Scraper()
    competitors = ['Grab', 'Deliveroo', 'Uber', 'Google', 'Gofood']
    iterations = int(sys.argv[1])

    # Cleanup status file
    write_file({}, file_path)

    # Start driver program
    for i in range(iterations):
        print(f"Start of iteration {i+1}")
        for competitor in competitors:
            avoidable_ip_address_list = cheetah(competitor, file_path)
            
            ip_address, competitor_name, execution_time = scraper.execute_scraper_lambda(
                avoidable_ip_address_list=avoidable_ip_address_list,
                competitor_name=competitor
            )
            if ip_address and execution_time:
                record_ip_status(ip_address, competitor_name, file_path)
            print(f"Competitor name - {competitor}, Avoidable IP list - {avoidable_ip_address_list}, Execution IP - {ip_address}, Execution Time - {execution_time}")
        print(f"End of iteration {i+1}\n")
