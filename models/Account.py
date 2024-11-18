from peewee import Model, CharField, IntegerField, DateTimeField, AutoField
from datetime import datetime
from config import db

# Account Model
class Account(Model):
    key = AutoField()
    nametag = CharField(unique=True, null=False)
    user = CharField(unique=True, null=False)
    password = CharField(null=False)
    banida = IntegerField(null=False)
    idCompra = CharField(null=False)
    email = CharField()
    elo = CharField()
    ultimaAtividade = CharField()
    dataRegistro = DateTimeField(default=datetime.now)

    class Meta:
        database = db  # Associa o modelo ao banco de dados
        
# Criar a tabela 'Usuario' apenas se ela não existir
db.connect()
db.create_tables([Account], safe=True)
db.close()