from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

COINDESK_CZK_URL = "https://api.coindesk.com/v1/bpi/currentprice/CZK.json"
COINDESK_EUR_URL = "https://api.coindesk.com/v1/bpi/currentprice/EUR.json"

@app.route('/btc-price', methods=['GET'])
def get_btc_price():
    response_czk = requests.get(COINDESK_CZK_URL).json()
    response_eur = requests.get(COINDESK_EUR_URL).json()

    btc_price_czk = response_czk['bpi']['CZK']['rate_float']
    btc_price_eur = response_eur['bpi']['EUR']['rate_float']

    server_time_czk = response_czk['time']['updatedISO']
    server_time_eur = response_eur['time']['updatedISO']

    return jsonify({
        'btc_price_czk': btc_price_czk,
        'btc_price_eur': btc_price_eur,
        'currency_czk': 'CZK',
        'currency_eur': 'EUR',
        'client_request_time': datetime.utcnow().isoformat(),
        'server_data_time_czk': server_time_czk,
        'server_data_time_eur': server_time_eur
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
