from .signals.initsignal import InitSignal
from .signals.startsignal import StartSignal
from .signals.endsignal import EndSignal


class SignalsFactory:

    @staticmethod
    def create_signal(signal_name):
        if signal_name == "init":
            return InitSignal(signal_name)
        
        elif signal_name == "start":
            return StartSignal(signal_name)

        elif signal_name == "end":
            return EndSignal(signal_name)

