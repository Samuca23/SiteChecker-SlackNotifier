# Use a imagem oficial do Python 3.9
FROM python:3.9

# Define a variável de ambiente PYTHONUNBUFFERED para garantir que a saída do Python seja exibida imediatamente sem buffer
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de código-fonte para o diretório de trabalho do contêiner
COPY . /app

# Instala as dependências do Python especificadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar o script quando o contêiner for iniciado
CMD ["python", "app.py"]
