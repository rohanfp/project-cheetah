from .signals.initsignal import InitSignal
from .signals.startsignal import StartSignal
from .signals.endsignal import EndSignal


class SignalsFactory:
    @staticmethod
    def create_signal(signal_name, service_name, ip_address):
        if signal_name == "INIT":
            return InitSignal(signal_name, service_name, ip_address)
        
        elif signal_name == "START":
            return StartSignal(signal_name, service_name, ip_address)

        elif signal_name == "END":
            return EndSignal(signal_name, service_name, ip_address)
