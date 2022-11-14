import socket


def cezar(key, text):
    key = key  # слухаємо і приймаємо потік даних
    text = text
    print(f'>> Шифрування з кроком {key} інформації: {text}')
    crypto_text = ''
    for symbol in text:
        if symbol.isalpha():
            crypto_text += chr((ord(symbol) + int(key)) % 123)
        else:
            crypto_text += symbol

    return crypto_text


class MyServer:
    @staticmethod
    def start_tcp():
        #  TCP Protocol
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(('localhost', 65000))
            server.listen(1)
            # Приймаємо користувача
            user, address = server.accept()

            with user:
                print('Connection Address is: ', address)
                while True:
                    # слухаємо, приймаємо та декодуєм потік даних
                    key = user.recv(1024).decode("utf-8")
                    text = user.recv(1024).decode("utf-8")
                    if not key:
                        break
                    user.send(cezar(key, text).encode("utf-8"))

    @staticmethod
    def start_udp():
        # TCP Protocol
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.bind(('localhost', 65000))

            crypto = []

            # Приймаємо дані
            while len(crypto) < 2:
                data, address = server.recvfrom(1024)
                crypto.append(data.decode("utf-8"))

            server.sendto(cezar(crypto[0], crypto[1]).encode("utf-8"), address)
        server.close()


if __name__ == '__main__':
    if input('1 - tcp сервер, 2 - udp сервер: ') == 1:
        MyServer.start_tcp()
    else:
        MyServer.start_udp()