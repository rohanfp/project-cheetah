from .rule import Rule


class RecentlyUsedIpRule(Rule):
    def handler(self, data=None):
        service_level_status_data = data['service_level_status']
        service_name = data['service_name']
        temp_ip_list = [item for item in service_level_status_data if item['ip_address'] in data['result']]
        temp_ip_list = sorted(temp_ip_list, key=lambda x: x['latest_end_timestamp'])
        data['result'] = [item['ip_address'] for item in temp_ip_list]
        return super().handler(data)
