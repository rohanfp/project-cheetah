from .signal import Signal


class StartSignal(Signal):
    def perform(self):
        pass

    def log(self):
        return f"{self.signal_name}_{self.service_name}_{self.ip_address}_{self.timestamp}"
