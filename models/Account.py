from peewee import Model, CharField, IntegerField, DateTimeField, AutoField
from datetime import datetime
from config import db



# Account Model
class Account(Model):
    key = AutoField()
    user = CharField(unique=True, null=False)
    password = CharField(null=False)
    nametag = CharField(unique=True, null=False)
    email = CharField()
    elo = CharField()
    ultimaAtividade = CharField()
    banida = IntegerField(null=False)
    idCompra = CharField(null=False, unique=True)
    
    dataRegistro = DateTimeField(default=datetime.now)
    dataAtualizacao = DateTimeField(default=datetime.now)

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        self.dataAtualizacao = datetime.now()
        return super().save(*args, **kwargs)
    
# Criar a tabela 'Usuario' apenas se ela não existir
db.connect()
db.create_tables([Account], safe=True)
db.close()