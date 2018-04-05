import socket
PROMPT = ">>"
# porta padrão definida para comunicação
sPORT = 3000


class Cliente:
    def __init__(self):
        # inicializa soquete
        self.sock = socket.socket()

    def conectar(self, ip, porta):
        addr = (ip, porta)
        print(ip)
        print(porta)
        self.sock.connect(addr)
        while True:
            msg = input(PROMPT)
            self.sock.send(msg.encode())
            if(msg == "sair"):
                break
        self.sock.close()


def main():
    ip = input("Digite o ip para qual se conectar: ")
    if(ip.count(".") != 3):
        print("Entrada inválida")
        main()
    else:
        novo_cliente = Cliente().conectar(ip, sPORT)


if __name__ == "__main__":
    main()
