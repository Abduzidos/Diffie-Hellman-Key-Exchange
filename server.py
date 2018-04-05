import socket

sPORT = 3000


class Server:
    def __init__(self, ip):
        self.sock = socket.socket()
        self.ip = ip
        self.buf = 1024

    def iniciar(self, port):
        addr = (self.ip, port)
        self.sock.bind(addr)
        self.sock.listen(1)
        conn, addre = self.sock.accept()
        print("Connection from: " + str(addre))
        while True:
            msg = conn.recv(self.buf).decode()
            print(str(msg))
            # self.sock.send(msg.encode())
            # conn.send(msg.encode())
            if(msg == "sair"):
                break
        self.sock.close()


def main():
    ip = input("Digite o ip do server: ")
    if(ip.count(".") != 3):
        print("Entrada inválida")
        main()
    else:
        servidor = Server(ip)
        servidor.iniciar(sPORT)


if __name__ == "__main__":
    main()
