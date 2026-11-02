from cryptography.fernet import Fernet

# 1. Carrega a chave de segurança salva anteriormente
try:
    with open("chavesinha.key", "rb") as chave_arquivo:
        chave = chave_arquivo.read()
    print("[+] Chave carregada com sucesso!")
except FileNotFoundError:
    print("[-] Erro: Chave de segurança não encontrada!")
    exit()

# 2. Define o arquivo alvo
nome_arquivo = "teste.txt"

# 3. Lê o conteúdo criptografado
with open(nome_arquivo, "rb") as arquivo:
    conteudo_criptografado = arquivo.read()

# 4. Descriptografa os dados usando a chave
f = Fernet(chave)
conteudo_descriptografado = f.decrypt(conteudo_criptografado)

# 5. Restaura o arquivo original
with open(nome_arquivo, "wb") as arquivo:
    arquivo.write(conteudo_descriptografado)

print("[+] SUCESSO! O arquivo foi descriptografado e o texto original foi restaurado!")