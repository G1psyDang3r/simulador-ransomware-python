import os
from cryptography.fernet import Fernet

# 1. Gera e salva a chave de segurança localmente
chave = Fernet.generate_key()
with open("chavesinha.key", "wb") as chave_arquivo:
    chave_arquivo.write(chave)

print("[+] Chave de segurança gerada com sucesso!")

# 2. Cria um arquivo de teste simulando um documento alvo
nome_arquivo = "teste.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Este é um arquivo secreto importante! Se você está lendo isso, os dados foram criptografados.")
print(f"[+] Arquivo '{nome_arquivo}' criado para o teste.")

# 3. Lê o conteúdo original do arquivo
with open(nome_arquivo, "rb") as arquivo:
    conteudo = arquivo.read()

# 4. Criptografa o conteúdo
f = Fernet(chave)
conteudo_criptografado = f.encrypt(conteudo)

# 5. Sobrescreve o arquivo com os dados criptografados (ilegíveis)
with open(nome_arquivo, "wb") as arquivo:
    arquivo.write(conteudo_criptografado)

print("[!] ALERTA: O arquivo foi criptografado com sucesso!")

# 6. Cria a Nota de Resgate simulada
with open("LEIA_ISSO.txt", "w", encoding="utf-8") as aviso:
    aviso.write("SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!\n")
    aviso.write("Para recuperá-los, utilize a chave de descriptografia gerada no ambiente de testes.\n")

print("[*] Nota de resgate 'LEIA_ISSO.txt' gerada na pasta.")