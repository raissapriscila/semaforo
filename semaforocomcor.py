import time
from colorama import Fore, init

init()

while True:
    print(Fore. + 'semaforo vermelho')
    print(Fore.RED + 'nao atravessar')
    time.sleep(5)

    print(Fore.YELLOW + 'semaforo amarelo')
    print(Fore.YELLOW + 'muita atenção')
    time.sleep(2)

    print(Fore.GREEN + 'semaforo verde')
    print(Fore.GREEN + 'pode atravessar')
    time.sleep(5)