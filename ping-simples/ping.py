import os


print('#' * 60)
ip_ou_host = input('Digite o IP ou host as ser verificados: ')

print('-' * 60)

os.system('ping -c 6 {}'.format(ip_ou_host))