from services import criar_account, obter_accounts, atualizar_account_id
from flask import Flask, request, jsonify
import subprocess
import os


app = Flask(__name__)


@app.route('/api/account', methods=['POST'])
def criar_account():
    # Obtendo json
    dados = request.get_json()

    # Criar account
    criar_account(**dados)

    # Processar os dados conforme necessário
    return jsonify({"mensagem": "Conta criada com sucesso!"}), 200


@app.route('/api/account', methods=['PUT'])
def atualizar_account():
    # Obtendo json
    dados = request.get_json()

    # Criar account
    atualizar_account_id(**dados)

    # Processar os dados conforme necessário
    return jsonify({"mensagem": "Conta atualizada com sucesso!"}), 200


@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    # Criar account
    accounts = obter_accounts()
    print(accounts)
    # Processar os dados conforme necessário
    return jsonify({'data': accounts}), 200


if __name__ == '__main__':
    app.run(debug=True)