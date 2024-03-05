import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time

site_url = ['https://www.unidvi.edu.br', 'https://www.alura.com.br']

slack_channel = '#verifica_sites'

slack_token = ''

def check_site_status(url):
    """
    Endpoit para verificar o status do site.
    """
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def send_slack_message(message, channel, token):
    """
    Endpoit para fazer o envio da mensagem.
    """
    client = WebClient(token=token)
    try:
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Erro ao enviar mensagem para o Slack: {e.response['error']}")

if __name__ == '__main__':
    print("Iniciando verificação de sites")
    while True:
        for site in site_url:
            if not check_site_status(site):
                send_slack_message(f'O site {site} está offline!', slack_channel, slack_token)
            time.sleep(10) 
