import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print('A conexão falhou!!!')
        print(f'Erro: {error}')
        sys.exit()
    
    print('Socket criado com sucesso')

    host_alvo = input('Digite o Host ou Ip: ')
    porta_alvo = int(input('Digite a porta: '))

    try:
        s.connect((host_alvo, porta_alvo))
        print(f'Cliente TCP conectado com sucesso no Host: {host_alvo} Porta: {porta_alvo}.')
        s.shutdown(2)
    except socket.error as error:
        print('A conexão falhou!!!')
        print(f'Erro: {error}')
        sys.exit()


if __name__ == '__main__':
    main()