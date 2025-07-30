# Importando as bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo o arquivo Excel 
data = pd.read_excel('../dados_ficticios_produtos.xlsx', None)

# Acessando a planilha que contém os dados
df = data['Sheet1']

# Filtrando apenas os dados das Lojas
loja_a = df[df['Loja'] == 'Loja A']
loja_b = df[df['Loja'] == 'Loja B']
loja_c = df[df['Loja'] == 'Loja C']
loja_d = df[df['Loja'] == 'Loja D']

# Calculando o lucro total da Loja 
lucro_total_A = loja_a['Preço Total'].sum()
lucro_total_B = loja_b['Preço Total'].sum()
lucro_total_C = loja_c['Preço Total'].sum()
lucro_total_D = loja_d['Preço Total'].sum()

print(f"Lucro total da Loja A: R${lucro_total_A:,.2f}")
print("==")
print(f"Lucro total da Loja B: R${lucro_total_B:,.2f}")
print("==")
print(f"Lucro total da Loja C: R${lucro_total_C:,.2f}")
print("==")
print(f"Lucro total da Loja D: R${lucro_total_D:,.2f}")
