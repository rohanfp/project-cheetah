from .signal import Signal


class EndSignal(Signal):
    def perform(self):
        print(self.signal_name)

    def log(self):
        pass
