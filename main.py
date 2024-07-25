from cryptography.fernet import Fernet
import os

# Caminho fixo para o arquivo CSV e o arquivo criptografado
CSV_FILE_PATH = 'teste.csv'
ENCRYPTED_FILE_PATH = CSV_FILE_PATH + '.enc'
DECRYPTED_FILE_PATH = CSV_FILE_PATH + '.dec.csv'

def generate_key():
    """Gera uma nova chave de criptografia e a salva em um arquivo."""
    key = Fernet.generate_key()  # Gera uma nova chave de criptografia
    with open('mykey.key', 'wb') as key_file:  # Abre o arquivo de chave para escrita em modo binário
        key_file.write(key)  # Salva a chave no arquivo
    print("Chave gerada e salva como 'mykey.key'.")

def load_key():
    """Carrega a chave de criptografia de um arquivo."""
    if os.path.exists('mykey.key'):  # Verifica se o arquivo de chave existe
        with open('mykey.key', 'rb') as key_file:  # Abre o arquivo de chave para leitura em modo binário
            return key_file.read()  # Lê e retorna a chave
    else:
        raise FileNotFoundError("O arquivo de chave 'mykey.key' não foi encontrado.")

def encrypt_csv():
    """Criptografa o conteúdo de um arquivo CSV fixo e salva o conteúdo criptografado em um novo arquivo."""
    # Carrega a chave
    key = load_key()  # Carrega a chave de criptografia
    fernet = Fernet(key)  # Inicializa o objeto Fernet com a chave

    # Lê o conteúdo do arquivo CSV
    if os.path.exists(CSV_FILE_PATH):  # Verifica se o arquivo CSV existe
        with open(CSV_FILE_PATH, 'rb') as file:  # Abre o arquivo CSV para leitura em modo binário
            csv_data = file.read()  # Lê o conteúdo do arquivo

        # Criptografa o conteúdo do arquivo CSV
        encrypted_data = fernet.encrypt(csv_data)  # Criptografa os dados do arquivo CSV

        # Salva o conteúdo criptografado em um novo arquivo
        with open(ENCRYPTED_FILE_PATH, 'wb') as file:  # Abre o arquivo criptografado para escrita em modo binário
            file.write(encrypted_data)  # Salva o conteúdo criptografado no arquivo
        
        print(f"Arquivo CSV criptografado salvo como '{ENCRYPTED_FILE_PATH}'.")
    else:
        print(f"O arquivo '{CSV_FILE_PATH}' não foi encontrado.")

def decrypt_csv():
    """Descriptografa o conteúdo de um arquivo CSV criptografado fixo e salva o conteúdo descriptografado em um novo arquivo."""
    # Carrega a chave
    key = load_key()  # Carrega a chave de criptografia
    fernet = Fernet(key)  # Inicializa o objeto Fernet com a chave

    # Lê o conteúdo do arquivo CSV criptografado
    if os.path.exists(ENCRYPTED_FILE_PATH):  # Verifica se o arquivo criptografado existe
        with open(ENCRYPTED_FILE_PATH, 'rb') as file:  # Abre o arquivo criptografado para leitura em modo binário
            encrypted_data = file.read()  # Lê o conteúdo do arquivo criptografado

        # Descriptografa o conteúdo do arquivo CSV
        decrypted_data = fernet.decrypt(encrypted_data)  # Descriptografa os dados do arquivo criptografado

        # Salva o conteúdo descriptografado em um novo arquivo
        with open(DECRYPTED_FILE_PATH, 'wb') as file:  # Abre o arquivo descriptografado para escrita em modo binário
            file.write(decrypted_data)  # Salva o conteúdo descriptografado no arquivo
        
        print(f"Arquivo CSV descriptografado salvo como '{DECRYPTED_FILE_PATH}'.")
    else:
        print(f"O arquivo '{ENCRYPTED_FILE_PATH}' não foi encontrado.")

def main():
    """Função principal que permite ao usuário escolher uma ação."""
    print("1. Gerar nova chave")  # Opção para gerar uma nova chave
    print("2. Criptografar arquivo CSV")  # Opção para criptografar o arquivo CSV
    print("3. Descriptografar arquivo CSV")  # Opção para descriptografar o arquivo CSV
    choice = input("Escolha uma opção (1, 2 ou 3): ")  # Recebe a escolha do usuário

    if choice == '1':
        generate_key()  # Chama a função para gerar uma nova chave
    elif choice == '2':
        encrypt_csv()  # Chama a função para criptografar o arquivo CSV
    elif choice == '3':
        decrypt_csv()  # Chama a função para descriptografar o arquivo CSV
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")  # Mensagem de erro para opção inválida

if __name__ == "__main__":
    main()  # Executa a função principal quando o script é executado
