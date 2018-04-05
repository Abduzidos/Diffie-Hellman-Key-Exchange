# The main formula is A = (G**a) % P
# To get the final key you use the same formula, with different variables S = (A**a) % P
from Cliente import *

def apply_dh_formula(G, a, P):
    return (G**a) % P

def conectar():
    ip = input("Digite o ip para qual se conectar: ")
    if(ip.count(".") != 4):
        print("Entrada inválida")
        receberIp()
    else:
        novo_cliente = Cliente().conectar(sPORT,ip)

def main():
    # Variables to Test, it will be sent in the communication
    REMOTE_G = 5
    REMOTE_P = 3

    # Just to test, IT WILL NOT EXIST AND NOT WILL BE SENT IN THE VERSION WITH COMMUNICATION
    REMOTE_a = 12128109

    # Getting the G param
    LOCAL_G = int(input(
        'Choose a number between 0 to 99 a index for your G in the prime number table: '))
    while LOCAL_G not in range(0, 99):
        LOCAL_G = int(input(
            'Choose a number between 0 to 99 a index for your G in the prime number table: '))

    # Getting the P param
    LOCAL_P = int(input(
        'Choose a number between 0 to 99 a index for your P in the prime number table: '))
    while LOCAL_P not in range(0, 99):
        LOCAL_P = int(input(
            'Choose a number between 0 to 99 a index for your P in the prime number table: '))

    if(LOCAL_G != REMOTE_G):
        print("You should come to consensus about the G number")
        return

    if(LOCAL_P != REMOTE_P):
        print("You should come to consensus about the P number")
        return

    LOCAL_a = int(input(
        'Choose a number to be your local private key (the little a): '))

    A = apply_dh_formula(LOCAL_G, LOCAL_a, LOCAL_P)
    print(A)

    conectar()
if __name__ == "__main__":
    main()
