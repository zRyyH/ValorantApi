# Usa uma imagem Python como base
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para o container
COPY . /app

# Instala o Apache
RUN apt-get update

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe as portas para acesso externo
EXPOSE 3000

# Define o comando para iniciar o Gunicorn
CMD gunicorn -w 4 -b 0.0.0.0:3000 app:app