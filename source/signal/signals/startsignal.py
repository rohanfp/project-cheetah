from .signal import Signal


class StartSignal(Signal):
    def perform(self):
        print(self.signal_name)

    def log(self):
        pass
