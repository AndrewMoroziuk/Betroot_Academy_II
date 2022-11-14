import socket


class MyClient:
    @staticmethod
    def tcp_client():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            client.connect(('localhost', 65000))

            key = input("Ведіть ключ: ")
            text = input("Ведіть текст: ")

            client.sendall(key.encode("utf-8"))  # відправляємо потік даних
            client.sendall(text.encode("utf-8"))  # відправляємо потік даних

            in_data = client.recv(1024)  # слухаємо і приймаємо потік даних
            print("Зашифрований текст >>", in_data.decode("utf-8"))

    @staticmethod
    def udp_client():
        sockaddr = ('localhost', 65000)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            # client.connect(('localhost', 65000))

            key = input("Ведіть ключ: ")
            text = input("Ведіть текст: ")

            client.sendto(key.encode("utf-8"), sockaddr)  # відправляємо потік даних
            client.sendto(text.encode("utf-8"), sockaddr)  # відправляємо потік даних

            data, address = client.recvfrom(1024)
            print("Зашифрований текст >>", data.decode("utf-8"))


if __name__ == '__main__':
    if input('1 - tcp клієнт, 2 - udp клієнт: ') == 1:
        MyClient.tcp_client()
    else:
        MyClient.udp_client()
