from .translator import Translator

class SnsTranslator(Translator):
    def translate(self, message):
        self.message = message
        try:
            self.translated_message = {
                'signal_name': message['Records'][0]['Sns']['Message']['signalName'],
                'ip_address': message['Records'][0]['Sns']['Message']['ipAddress'],
                'scraper_type': message['Records'][0]['Sns']['Message']['scraperType'],
                'service_name': message['Records'][0]['Sns']['Message']['serviceName'] if 'serviceName' in message['Records'][0]['Sns']['Message'] else None,
                'time': message['Records'][0]['Sns']['Message']['time'] if 'time' in message['Records'][0]['Sns']['Message'] else None
            }
        except Exception:
            self.translated_message = { **message['Records'][0]['Sns']['Message'] }
        return self.translated_message
