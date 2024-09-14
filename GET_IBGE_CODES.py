import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Inicializando uma lista para armazenar os resultados
table_data = []

# Função para obter o tópico da tabela
def get_table_topic(table_number):
    url = f"https://sidra.ibge.gov.br/tabela/{table_number}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        topic = soup.find('title').get_text()  # Ajuste baseado no tag correto
        return topic
    else:
        return "Not available"

# Loop através dos números das tabelas
for table_num in range(1, 9350):
    topic = get_table_topic(table_num)
    table_data.append([table_num, topic])
    
    # Exibindo progresso a cada 100 tabelas
    if table_num % 100 == 0:
        print(f"Progresso: {table_num}/9349 tabelas processadas.")
    

# Criando o DataFrame
df = pd.DataFrame(table_data, columns=['Table Number', 'Topic'])

# Salvando em CSV
df.to_csv('sidra_table_topics.csv', index=False)

# Exibindo DataFrame
print(df.head())




# Assuming 'Title' is the column where the "série encerrada" message appears
df_filtered = df[~df['Topic'].str.contains("série encerrada", case=False, na=False)]

# Display the filtered DataFrame
print(df_filtered.head())

