from models import Account

def criar_account(
        user: str, 
        password: str, 
        nametag: str, 
        idCompra: str,
        email: str = 'Não Definido', 
        elo: str = 'Não Definido', 
        ultimaAtividade: int = 0, 
        banida: int = 0):
    
    usuario = Account.create(
        user=user,
        password=password,
        nametag=nametag,
        idCompra=idCompra,
        email=email,
        elo=elo,
        ultimaAtividade=ultimaAtividade,
        banida=banida)
    
    return usuario

def atualizar_account_id(
        key: int, 
        user: str, 
        password: str, 
        nametag: str, 
        idCompra: str,
        email: str = 'Não Definido', 
        elo: str = 'Não Definido', 
        ultimaAtividade: int = 0, 
        banida: int = 0):

    query = Account.update(
        user=user,
        password=password,
        nametag=nametag,
        idCompra=idCompra,
        email=email,
        elo=elo,
        ultimaAtividade=ultimaAtividade,
        banida=banida).where(Account.key == key)

    query.execute()
    
def obter_accounts():
    return list(Account.select())