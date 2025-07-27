import pandas as pd
import random
from faker import Faker

# Inicializa o gerador de dados falsos
fake = Faker('pt_BR')

# Gera 100 linhas de dados fictícios
data = []
for _ in range(10000):
    nome = fake.name()
    idade = random.randint(18, 80)
    email = fake.email()
    telefone = fake.phone_number()
    cidade = fake.city()
    estado = fake.estado_sigla()
    data.append([nome, idade, email, telefone, cidade, estado])

# Cria o DataFrame
df = pd.DataFrame(data, columns=["Nome", "Idade", "Email", "Telefone", "Cidade", "Estado"])

# Salva como arquivo Excel
file_path = "../dados_ficticios.xlsx"
df.to_excel(file_path, index=False)
file_path
