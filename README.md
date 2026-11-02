# 🛡️ Projeto Prático: Simulação Controlada de Ransomware e Defesa Cibernética

Projeto desenvolvido como parte do bootcamp de Cibersegurança da [DIO](https://www.dio.me/) para fins exclusivamente educacionais, abrangendo o funcionamento de criptografia aplicada a ameaças e estratégias de mitigação.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada para a criação de scripts.
- **Biblioteca `cryptography` (Fernet)**: Utilizada para aplicar criptografia simétrica de ponta a ponta em arquivos de teste.

## 📂 Estrutura do Repositório

O projeto está organizado com os seguintes arquivos principais:

- `ransomware.py`: Script responsável por gerar a chave de segurança, criar um arquivo de alvo (`teste.txt`), criptografar seu conteúdo e gerar uma nota de resgate simulada (`LEIA_ISSO.txt`).
- `descriptografar.py`: Script de recuperação responsável por ler a chave de segurança e restaurar o arquivo original para seu estado legível.
- `chavesinha.key`: Arquivo contendo a chave simétrica gerada durante o processo de criptografia.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para testar a simulação de forma controlada em seu ambiente local:

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em sua máquina. Em seguida, instale a biblioteca de criptografia necessária executando o comando abaixo no terminal:

```bash
pip install cryptography

```

### 2. Executando a Simulação (Criptografia)

O script `ransomware.py` criará um arquivo de teste (`teste.txt`), gerará a chave de segurança (`chavesinha.key`), criptografará o conteúdo do arquivo e deixará a nota de resgate simulada (`LEIA_ISSO.txt`).

Execute o script:

```bash
python ransomware.py

```

> **O que observar:** Verifique que o arquivo `teste.txt` terá seu conteúdo original criptografado e que os arquivos de chave e nota de resgate foram gerados no diretório.

### 3. Recuperando os Dados (Descriptografia)

Para reverter o processo e restaurar o arquivo original utilizando a chave gerada, execute o script de recuperação:

```bash
python descriptografar.py

```

> **O que observar:** O script fará a leitura da chave em `chavesinha.key`, descriptografará o `teste.txt` e retornará o conteúdo original do arquivo ao seu estado legível.
