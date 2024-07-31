from config.settings import T_TOKEN
import requests


class MyBot:

    URL = 'https://api.telegram.org/bot'
    TOKEN = T_TOKEN

    def send_message(self, chat_id, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )