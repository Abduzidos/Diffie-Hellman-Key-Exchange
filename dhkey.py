import socket
import threading
LOCAL_P = 0
LOCAL_G = 0
a = 0
flag = 0
ENCODING = 'utf-8'


class Receiver(threading.Thread):
    def __init__(self, my_host, my_port):
        threading.Thread.__init__(self, name="messenger_receiver")
        self.host = my_host
        self.port = my_port

    def apply_dh_formula(self, G, a, P):
        return (G**a) % P

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global LOCAL_G
        global LOCAL_P
        global a
        REMOTE_A = 0
        global flag
        sock.bind((self.host, self.port))
        sock.listen(10)
        while True:
            connection, client_address = sock.accept()
            try:
                full_message = ""
                while True:
                    data = connection.recv(16)
                    full_message = full_message + data.decode(ENCODING)
                    # Pode ser, mas t   alvez o professor queira que os dois entrem em consens
                    if not data:
                        # print("{}".format(full_message.strip()))
                        full_message = ""
                        break
                    if "G: " in full_message and LOCAL_G == 0:
                        LOCAL_G = full_message.split('G: ')
                        LOCAL_G = int(LOCAL_G[-1])
                        #print("MEU LOCAL G")
                        # print(LOCAL_G)
                        full_message = ""

                    if "P: " in full_message and LOCAL_P == 0:
                        LOCAL_P = full_message.split('P: ')
                        LOCAL_P = int(LOCAL_P[-1])
                        #print("MEU LOCAL P")
                        # print(LOCAL_P)
                        full_message = ""

                    if "A: " in full_message and REMOTE_A == 0:
                        REMOTE_A = full_message.split('A: ')
                        REMOTE_A = int(REMOTE_A[-1])
                        #print("MEU REMOTE A")
                        # print(REMOTE_A)
                        full_message = ""
                        S = self.apply_dh_formula(REMOTE_A, a, LOCAL_P)
                        print("MY SECURITY KEY IS:", S)

            finally:
                # connection.shutdown(2)
                connection.close()

    def run(self):
        self.listen()


class Sender(threading.Thread):

    def __init__(self, my_friends_host, my_friends_port):
        threading.Thread.__init__(self, name="messenger_sender")
        self.host = my_friends_host
        self.port = my_friends_port

    def apply_dh_formula(self, G, a, P):
        return (G**a) % P

    def run(self):
        global LOCAL_P
        global LOCAL_G
        global flag
        ALREADY_SENT = 0
        while True:
            message = input("")
            if "P: " in message:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                s.sendall(message.encode(ENCODING))
                LOCAL_P = int(message.strip('P: '))
                # s.shutdown(2)
                s.close()
            if "G: " in message:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                s.sendall(message.encode(ENCODING))
                LOCAL_G = int(message.strip('G: '))
                # s.shutdown(2)
                s.close()

            if LOCAL_P != 0 and LOCAL_G != 0 and flag == 0:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                s.sendall(message.encode(ENCODING))
                A = self.apply_dh_formula(LOCAL_G, a, LOCAL_P)
                flag = 1
                A_TOSEND = "A: " + str(A)
                #s.sendall("A: ".encode(ENCODING))
                s.sendall(A_TOSEND.encode(ENCODING))
                ALREADY_SENT = 1
                # s.shutdown(2)
                s.close()


def main():
    global a
    # my_host = input("My HOST: ")
    my_host = 'localhost'
    my_port = int(input("My PORT: "))
    receiver = Receiver(my_host, my_port)
    #my_friends_host = input("Peer's HOST: ")
    my_friends_host = 'localhost'
    my_friends_port = int(input("Peer's PORT: "))
    a = int(input('Choose a number to be your local private key (the little a): '))
    sender = Sender(my_friends_host, my_friends_port)
    treads = [receiver.start(), sender.start()]


if __name__ == '__main__':
    main()
