from .signal.signalsfactory import SignalsFactory


def cheetah(signal_name, service_name, ip_address):
    signal = SignalsFactory().create_signal(signal_name, service_name, ip_address)
    response = signal.perform()
    return response