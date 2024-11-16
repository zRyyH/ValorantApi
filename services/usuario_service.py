from models import Account

def criar_account(
        user: str, 
        password: str, 
        nametag: str, 
        idCompra: str = 'Não Definido',
        email: str = 'Não Definido', 
        elo: str = 'Não Definido', 
        ultimaAtividade: str = 'Não Definido', 
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
        idCompra: str = 'Não Definido',
        email: str = 'Não Definido', 
        elo: str = 'Não Definido', 
        ultimaAtividade: str = 'Não Definido', 
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
    query = Account.select()

    # Converter para dicionários:
    dados = list(query.dicts())

    return dados