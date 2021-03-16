from .signal import Signal


class InitSignal(Signal):
    def perform(self):
        print(self.signal_name)

    def log(self):
        pass
