import os
import time
from datetime import datetime

def titulo(titulo): #Definindo titulo
    print("\033[36m" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50 + "\033[0m\n")



def limpar(): #limpa a tela
    os.system("cls")

def pausa(): #Tempo de pausa
    time.sleep(2)

def data(data_entrada): #Conversão de data DD/MM/AAAA para AAAA/MM/DD para o MySQL
    data_convertida = datetime.strptime(data_entrada, "%d/%m/%Y").date()
    return data_convertida


def sair():
    print("Saindo do sistema em 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")