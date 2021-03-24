from .translator import Translator

class SqsTranslator(Translator):
    def translate(self, message):
        self.message = message
        self.translated_message = message['Records'][0]['body']
        self.translated_message = {
            'signal_name': message['Records'][0]['body']['signalName'],
            'ip_address': message['Records'][0]['body']['ipAddress'],
            'scraper_type': message['Records'][0]['body']['scraperType'],
            'service_name': message['Records'][0]['body']['serviceName'] if 'serviceName' in message['Records'][0]['body'] else None,
            'time': message['Records'][0]['body']['time'] if 'time' in message['Records'][0]['body'] else None
        }
        return self.translated_message
