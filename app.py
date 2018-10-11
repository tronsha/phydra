import socket, time, string

def main():
    ircConnection = connect()
    while True:
        try:
            receivedData = ircConnection.recv(4096)
            if not receivedData: break
            receivedText = receivedData.decode("utf-8").strip()
            if receivedText is not '': 
                print(receivedText)
                splittedText = receivedText.split(' ', 1)
                if splittedText[0] == 'PING':
                    submitText = "PONG %s\n" % splittedText[1]
                    ircConnection.send(submitText.encode())
                    print(submitText.strip())
            time.sleep(.1)
        except socket.timeout:
            ircConnection = connect()

def connect():
    ircConnection = socket.create_connection(('chat.freenode.net', 6667), 600)
    ircConnection.send(b"USER Phydra * * :Phydra\n")
    ircConnection.send(b"NICK Phydra\n")
    return ircConnection

main()
