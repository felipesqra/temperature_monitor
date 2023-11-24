import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# Configurar a API do Kaggle com suas credenciais
kaggle.api.authenticate()

# Substitua 'nome_do_usuario/nome_do_conjunto_de_dados' pelo caminho do conjunto de dados que você deseja baixar
dataset_path = 'nelgiriyewithana/global-weather-repository'

# Baixar o conjunto de dados
kaggle.api.dataset_download_files(dataset_path, path='./data/', unzip=True)

