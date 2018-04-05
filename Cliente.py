import socket
PROMPT = ">>"
#porta padrão definida para comunicação
sPORT = 5000

class Cliente:
    def __init__(self):
        #inicializa soquete
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
    def conectar(self,ip,porta):
        addr = (ip,porta)
        self.sock.bind(addr)
        while True:
            msg = input(PROMPT)
            self.sock.sendto(msg.encode(),addr)
            if(msg == "sair"):
                break
        self.sock.close()


def main():
    
    cliente = Cliente()
    cliente.conectar(ip,sPORT)

if __name__ == "__main__":
    main()


    
