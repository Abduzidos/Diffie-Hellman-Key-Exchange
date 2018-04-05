import socket
class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = "192.168.0.22"
        self.buf = 1024
        
    def iniciar(self,port):
        addr = (self.ip,port)
        self.sock.bind(addr)
        
        while True:
            msg,cliente = self.sock.recvfrom(self.buf)
            print(msg)
            if(data == "sair"):
                break
        self.sock.close()

def main():
    servidor = Server()
    servidor.iniciar(5000)
if __name__ == "__main__":
    main()
        
        
