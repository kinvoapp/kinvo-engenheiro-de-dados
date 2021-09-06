# Instalando virutalenv
pip install virtualenv

# Criando ambiente
virtualenv environment

# Ativando virtualenv
echo "Ativando virtualenv..."
source environment/bin/activate

# Atualizando instalador
echo "Atualizando pip..."
pip install --upgrade pip

# Instalando dependencias
echo "Download de dependencias..."
pip install -r requirements.txt

# Download do dicionario de palavras
python -m spacy download pt_core_news_sm

# Criando container para renderização de paginas para o splash
echo "Iniciando container docker splash..."
docker run -name splash -d -it -p 8050:8050 scrapinghub/splash --max-timeout 300

# Executando servidor scrapy
echo "Executando servidor scrapy..."
cd ./mining
scrapyrt &
cd ..

# Executando servidor da aplicação
echo "Exercutando servidor aplicação..."
cd ./api
export FLASK_APP=server.py
flask run
