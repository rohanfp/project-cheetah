from .signal import Signal


class StartSignal(Signal):
    def perform(self, scraper_type, ip_address, service_name, timestamp):
        super().perform(scraper_type, ip_address, service_name, timestamp)
        table_name = 'ip-level-status'
        self.save_data(table_name)
