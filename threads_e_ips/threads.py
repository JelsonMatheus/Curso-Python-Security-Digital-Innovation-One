from threading import Thread
import time


def carro(nome, velocidade):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Carro: {nome} velocidade: {velocidade}. \n')



t_carro1 = Thread(target=carro, args=["carroA", 1])
t_carro2 = Thread(target=carro, args=["carroB", 1.5])

t_carro1.start()
t_carro2.start()