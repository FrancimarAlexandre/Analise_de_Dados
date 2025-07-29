# Importando as bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# lendo o arquivo excel
data = pd.read_excel('../dados_ficticios.xlsx',None)
# Criando o DataFrame
print(data.keys())
dados = {
    'preco': data['Sheet1']['Preço'],
    'quantidade': data['Sheet1']['Quantidade']
}
df = pd.DataFrame(dados)

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Exibindo estatísticas descritivas
print(df.describe())

# Plotando um gráfico de dispersão
sns.scatterplot(data=df, x='preco', y='quantidade')
plt.show()