from services import criar_account, obter_accounts, atualizar_account_id
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/api/account", methods=["POST"])
def account_post():
    # Obtendo json
    dados = request.get_json()

    # Criar account
    if data := criar_account(**dados):
        # Processar os dados conforme necessário
        return jsonify({"mensagem": "Conta criada com sucesso!"}), 200
    else:
        return jsonify({"mensagem": data}), 200


@app.route("/api/account", methods=["PUT"])
def account_put():
    # Obtendo json
    dados = request.get_json()

    # Criar account
    if data := atualizar_account_id(**dados):
        return jsonify({"mensagem": "Conta atualizada com sucesso!"}), 200
    else:
        return jsonify({"mensagem": data}), 200


@app.route("/api/accounts", methods=["GET"])
def account_get():
    # Criar account
    accounts = obter_accounts()

    if accounts := obter_accounts():
        # Processar os dados conforme necessário
        return jsonify(accounts), 200
    else:
        return jsonify({"mensagem": "Nenhuma conta encontrada!"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=3000)