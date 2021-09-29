import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

print('Clinte criado com Sucesso!')

host = 'localhost'
porta = 5432
mensagem = 'Ola servidor?'

try:
    print('Clinte: ' + mensagem)
    s.sendto(mensagem.encode(), (host, porta))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('\nCliente: ' + dados)
finally:
    print('Cliente: Fechando a conexão.')
    s.close()
