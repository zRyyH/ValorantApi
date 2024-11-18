from services import criar_account, obter_accounts, atualizar_account_id
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/api/account", methods=["POST"])
def account_post():
    # Obtendo json
    dados = request.get_json()

    # Criar account
    response = criar_account(**dados)

    if response["status"] == True:
        return jsonify({"mensagem": "Conta criada com sucesso!"}), 200
    else:
        return jsonify({"mensagem": response["error"]}), 500


@app.route("/api/account", methods=["PUT"])
def account_put():
    # Obtendo json
    dados = request.get_json()

    # Atualizar account
    response = atualizar_account_id(**dados)

    if response["status"] == True:
        return jsonify({"mensagem": "Conta atualizada com sucesso!"}), 200
    else:
        return jsonify({"mensagem": response["error"]}), 500


@app.route("/api/accounts", methods=["GET"])
def account_get():
    # Obter accounts
    response = obter_accounts()

    if response["status"] == True:
        return jsonify({"mensagem": response["result"]}), 200
    else:
        return jsonify({"mensagem": response["error"]}), 500


if __name__ == "__main__":
    app.run(debug=True, port=3000)