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

lista_lucro_total_A = list(loja_a['Preço Total'])
lista_lucro_total_B = list(loja_b['Preço Total'])
lista_lucro_total_C = list(loja_c['Preço Total'])
lista_lucro_total_D = list(loja_d['Preço Total'])
# gerando gráficos lucros

A = plt.plot(lista_lucro_total_A)
B = plt.plot(lista_lucro_total_B)
C = plt.plot(lista_lucro_total_C)
D = plt.plot(lista_lucro_total_D)
plt.title('Gráficos dos Lucros das lojas')
plt.xlabel("Quantidade")
plt.ylabel("valor")

plt.show()