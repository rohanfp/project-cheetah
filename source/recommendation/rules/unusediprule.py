from .rule import Rule


class UnusedIpRule(Rule):
    def handler(self, data=None):
        ip_level_status_data = data['ip_level_status']
        service_name = data['service_name']
        data['result'] = [item['ip_address'] for item in ip_level_status_data if service_name not in item['to_restrict_list']]
        super().handler(data)
