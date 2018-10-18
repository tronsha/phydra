import socket
import time
import _thread
import sys


def irc():
    irc_connection = connect()
    while True:
        try:
            received_data = irc_connection.recv(4096)
            if not received_data:
                break
            received_text = received_data.decode("utf-8").strip()
            if received_text is not '':
                print(received_text)
                split_text = received_text.split(' ', 1)
                if split_text[0] == 'PING':
                    submit_text = "PONG %s\n" % split_text[1]
                    irc_connection.send(submit_text.encode())
                    print(submit_text.strip())
            time.sleep(.1)
        except socket.timeout:
            break
        except ConnectionResetError:
            break
    sys.exit()


def connect():
    try:
        irc_connection = socket.create_connection(('chat.freenode.net', 6667), 600)
    except socket.error:
        return False
    irc_connection.send(b"USER Phydra * * :Phydra\n")
    irc_connection.send(b"NICK Phydra\n")
    return irc_connection


def setup():
    _thread.start_new_thread(irc, ())


def loop():
    time.sleep(1)


def main():
    setup()
    while True:
        loop()


main()
