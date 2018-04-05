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
        novo_cliente = Cliente().conectar(sPORT, ip)


def main():

     # Just to test, IT WILL NOT EXIST AND NOT WILL BE SENT IN THE VERSION WITH COMMUNICATION
    REMOTE_a = 121281

    # Variables to Test, it will be sent in the communication
    REMOTE_G = 179424691
    REMOTE_P = 179426549
    REMOTE_A = apply_dh_formula(REMOTE_G, REMOTE_a, REMOTE_P)

    # Getting the G param
    LOCAL_G = int(input(
        'Choose a number between 0 to 99 a index for your G in the prime number table: '))
    while LOCAL_G not in range(0, 179424692):
        LOCAL_G = int(input(
            'Choose a number between 0 to 99 a index for your G in the prime number table: '))

    # Getting the P param
    LOCAL_P = int(input(
        'Choose a number between 0 to 99 a index for your P in the prime number table: '))
    while LOCAL_P not in range(0, 179426550):
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

    # This A will be sent to the other pc
    A = apply_dh_formula(LOCAL_G, LOCAL_a, LOCAL_P)

    # This computer Part
    S = apply_dh_formula(REMOTE_A, LOCAL_a, LOCAL_P)

    # Just to test
    REMOTE_S = apply_dh_formula(A, REMOTE_a, REMOTE_P)

    print(A)
    print(REMOTE_S)
    print(S)

    conectar()


if __name__ == "__main__":
    main()
