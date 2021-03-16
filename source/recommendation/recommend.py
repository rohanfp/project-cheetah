class Engine:
    def __init__(self):
        pass
    
    def recommend_ip_address(self, status_data, service_name):
        ip_address = status_data[service_name]["queue"].pop(0)
        status_data[service_name]["queue"].append(ip_address)
        return ip_address
