#1. Importação de Dados

# Excel (com pacote readxl)
library(readxl)
dados <- read_excel("dados_ficticios.xlsx")

# 2. Exploração Inicial (EDA - Análise Exploratória de Dados)

# head(dados) # primeiras linhas

# str(dados) # estrutura

# summary(dados) # resumo estatístico 

# names(dados) # nome das colunas

# 3. Limpeza dos Dados

colSums(is.na(dados)) # verificar valores ausentes

dados_limpo <- na.omit(dados) # Remove linhas com NA

print(dados_limpo)