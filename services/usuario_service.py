from models import Account
import traceback


def criar_account(
    user: str,
    password: str,
    nametag: str,
    idCompra: str = "Não Definido",
    email: str = "Não Definido",
    elo: str = "Não Definido",
    ultimaAtividade: str = "Não Definido",
    banida: int = 0,
):

    try:
        Account.create(
            user=user,
            password=password,
            nametag=nametag,
            idCompra=idCompra,
            email=email,
            elo=elo,
            ultimaAtividade=ultimaAtividade,
            banida=banida,
        )

        return {"result": None, "status": True}
    except:
        return {"result": None, "status": False, "error": traceback.format_exc()}


def atualizar_account_id(
    key: int,
    user: str,
    password: str,
    nametag: str,
    idCompra: str = "Não Definido",
    email: str = "Não Definido",
    elo: str = "Não Definido",
    ultimaAtividade: str = "Não Definido",
    banida: int = 0,
):

    try:
        query = Account.update(
            user=user,
            password=password,
            nametag=nametag,
            idCompra=idCompra,
            email=email,
            elo=elo,
            ultimaAtividade=ultimaAtividade,
            banida=banida,
        ).where(Account.key == key)

        query.execute()

        return {"result": None, "status": True}
    except:
        return {"result": None, "status": False, "error": traceback.format_exc()}


def obter_accounts():
    try:
        query = Account.select()

        # Converter para dicionários:
        dados = list(query.dicts())

        return {"result": dados, "status": True}
    except:
        return {"result": None, "status": False, "error": traceback.format_exc()}