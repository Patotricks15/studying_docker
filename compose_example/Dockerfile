# Utiliza uma imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o diretório de trabalho
COPY . /app

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para acesso externo
EXPOSE 5000

# Define a variável de ambiente para o Flask identificar o arquivo da aplicação
ENV FLASK_APP=app.py

# Comando para iniciar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]