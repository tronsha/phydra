import socket
import time
import _thread
import sys


def irc(connection):
    while True:
        try:
            received_data = connection.recv(4096)
            if not received_data:
                break
            received_text = received_data.decode("utf-8").strip()
            if received_text is not '':
                print(received_text)
                split_text = received_text.split(' ', 1)
                if split_text[0] == 'PING':
                    submit_text = "PONG %s\n" % split_text[1]
                    connection.send(submit_text.encode())
                    print(submit_text.strip())
            time.sleep(.1)
        except socket.timeout:
            break
        except ConnectionResetError:
            break
    sys.exit()


def connect():
    try:
        connection = socket.create_connection(('chat.freenode.net', 6667), 600)
    except socket.error:
        return False
    connection.send(b"USER Phydra * * :Phydra\n")
    connection.send(b"NICK Phydra\n")
    return connection


def setup():
    _thread.start_new_thread(irc, (connect(),))


def loop():
    time.sleep(1)


def main():
    setup()
    while True:
        loop()


main()
