import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')

# Listas base para produtos
categorias = ['Eletrônicos', 'Alimentos', 'Roupas', 'Livros', 'Brinquedos', 'Beleza', 'Papelaria']
produtos = {
    'Eletrônicos': ['Mouse', 'Teclado', 'Monitor', 'Fone de Ouvido', 'Webcam'],
    'Alimentos': ['Arroz', 'Feijão', 'Macarrão', 'Café', 'Açúcar'],
    'Roupas': ['Camiseta', 'Calça', 'Vestido', 'Jaqueta', 'Meias'],
    'Livros': ['Romance', 'Biografia', 'Suspense', 'Didático', 'HQ'],
    'Brinquedos': ['Boneca', 'Carrinho', 'Quebra-Cabeça', 'Lego', 'Pelúcia'],
    'Beleza': ['Shampoo', 'Condicionador', 'Perfume', 'Maquiagem', 'Creme'],
    'Papelaria': ['Caderno', 'Caneta', 'Lápis', 'Borracha', 'Régua']
}
lojas = ['Loja A', 'Loja B', 'Loja C', 'Loja D']

data = []
for i in range(100):
    categoria = random.choice(categorias)
    nome_produto = random.choice(produtos[categoria])
    preco = round(random.uniform(5.0, 500.0), 2)
    custo = round(preco * random.uniform(0.5, 0.9), 2)
    quantidade = random.randint(1, 20)
    lucro_unitario = round(preco - custo, 2)
    preco_total = round(preco * quantidade, 2)
    data_venda = fake.date_between(start_date='-2y', end_date='today')
    loja = random.choice(lojas)

    data.append([
        i + 1,
        nome_produto,
        categoria,
        loja,
        data_venda,
        quantidade,
        custo,
        preco,
        lucro_unitario,
        preco_total
    ])

# Cria o DataFrame
df = pd.DataFrame(data, columns=[
    "ID do Produto", "Nome do Produto", "Categoria", "Loja", "Data de Venda",
    "Quantidade", "Custo Unitário", "Preço Unitário", "Lucro Unitário", "Preço Total"
])

# Salvando como arquivo Excel
file_path = "../dados_ficticios_produtos.xlsx"
df.to_excel(file_path, index=False)

file_path
