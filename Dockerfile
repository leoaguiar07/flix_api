# Define a imagem base
FROM python

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt /app

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia o código-fonte para o diretório de trabalho
COPY . .

#
EXPOSE 8000

# Define o comando de execução da API
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]