import socket, time, string, _thread 

def irc():
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
    try:
        ircConnection = socket.create_connection(('chat.freenode.net', 6667), 600)
    except:
        return False
    ircConnection.send(b"USER Phydra * * :Phydra\n")
    ircConnection.send(b"NICK Phydra\n")
    return ircConnection

def setup():
    _thread.start_new_thread(irc)

def loop():
    time.sleep(1)

def main():
    setup()
    while True:
        loop()
    return True

main()
