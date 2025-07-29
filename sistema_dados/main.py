import pandas as pd

from random import randint
data = []
for _ in range(100000):
    preco = randint(0.2,101.2)
    quantidade = randint(10,14)
    data.append([preco,quantidade])
# Cria o DataFrame
df = pd.DataFrame(data, columns=["Preço", "Quantidade"])

# Salva como arquivo Excel
file_path = "../dados_ficticios.xlsx"
df.to_excel(file_path, index=False)
file_path