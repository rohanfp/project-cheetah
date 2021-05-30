from .signal import Signal


class InitSignal(Signal):
    def perform(self, scraper_type, ip_address):
        super().perform(scraper_type, ip_address)
        table_name = 'ip-level-status'
        self.save_data(table_name)
