import csv
from .models import Dividend

def load_dividends_to_db(symbol):
    # Define o nome do arquivo CSV que está na raiz do projeto
    csv_filename = "PETR4.SA.csv"

    try:
        # Abre o arquivo CSV para leitura
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Obtenha os dados do CSV
                print(row)
                date = row.get('Date', '')
                dividends = row.get('Dividends', '')

                # Exemplo de como você pode dividir a data para obter o ano
                year = date.split('-')[0] if date else ''

                # Certifique-se de que 'year' e 'dividends' não sejam vazios
                if year and dividends:
                    # Crie um objeto Dividend no banco de dados
                    Dividend.objects.create(symbol=symbol, year=year, amount=float(dividends))
    except FileNotFoundError:
        print(f"O arquivo CSV '{csv_filename}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler e inserir dados do CSV: {e}")