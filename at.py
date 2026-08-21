brutos = [
    "joao.souza@EMAIL.com",
    "Rua das Flores, No 123",
    "000.111.222-33",
    "Carlos.ROCHA@ESCOLA.ORG",
    "Av. Central, No 450"
]

dados_limpos = []

for item in brutos:
    texto = item.strip()
    if "@" in texto:
        trxto = texto.lower()
    else:
        texto = texto.replace("No", "Número")
        texto = texto.replace(".", "").replace("-", "")
    dados_limpos.append(texto)

print("============================================")
print("     BASE DE DADOS TRATADA E SANITIZADA     ")
print("============================================")
for dado in dados_limpos:
    print("-", dado)