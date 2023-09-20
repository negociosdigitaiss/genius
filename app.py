from flask import Flask, jsonify
from telegram_extractor import extract_messages
from config import api_id, api_hash, channel01_username, channel02_username

app = Flask(__name__)

# Rota para extrair mensagens do canal 01
@app.route('/canal/channel01', methods=['GET'])
def get_channel01_messages():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    messages = extract_messages(client, channel01_username)
    client.disconnect()
    return jsonify(messages)

# Rota para extrair mensagens do canal 02
@app.route('/canal/channel02', methods=['GET'])
def get_channel02_messages():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    messages = extract_messages(client, channel02_username)
    client.disconnect()
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
