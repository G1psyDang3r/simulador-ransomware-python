# 🛡️ Projeto Prático: Simulação Controlada de Ransomware e Defesa Cibernética

Projeto desenvolvido como parte do bootcamp de Cibersegurança da [DIO](https://web.dio.me/lab/simulando-um-malware-de-captura-de-dados-simples-em-python-e-aprendendo-a-se-proteger/learning/dd3f8a01-98f9-48c9-9fc9-a68c23ae4bd5?back=/track/bootcamp-santander-ciberseguranca-do-zero-a-pratica) para fins exclusivamente educacionais, visando compreender o funcionamento de criptografia aplicada a ameaças e estratégias de mitigação.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**: Linguagem de programação utilizada para a criação dos scripts.
- **Biblioteca `cryptography` (Fernet)**: Utilizada para aplicar criptografia simétrica de ponta a ponta nos arquivos de teste.

---

## 📂 Estrutura do Repositório
O projeto está organizado com os seguintes arquivos principais:
- `ransomware.py`: Script responsável por gerar a chave de segurança, criar um arquivo de alvo (`teste.txt`), criptografar seu conteúdo e gerar a nota de resgate simulada (`LEIA_ISSO.txt`).
- `descriptografar.py`: Script de recuperação responsável por ler a chave de segurança e restaurar o arquivo original para o seu estado legível.
- `chavesinha.key`: Arquivo contendo a chave simétrica gerada durante o processo de criptografia.

---

## 🚀 Como Executar o Projeto

1. **Instale a dependência necessária:**
   ```bash
   pip install cryptography