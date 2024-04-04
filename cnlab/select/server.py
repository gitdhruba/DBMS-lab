import socket
import select

HOST = '127.0.0.1'
TCP_PORT = 5000
UDP_PORT = 5001

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind((HOST, TCP_PORT))
tcp_socket.listen(5)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, UDP_PORT))

sockets_list = [tcp_socket, udp_socket]

print(f'Server started. Listening on TCP port {TCP_PORT} and UDP port {UDP_PORT}')

while True:
    read_sockets, write_sockets, exception_sockets = select.select(sockets_list, [], [])

    for sock in read_sockets:
        if sock == tcp_socket:
            # Accept new TCP connection
            conn, addr = tcp_socket.accept()
            print(f'New TCP connection from {addr}')

            tcp_data = conn.recv(1024)
            if tcp_data:
                print(f'Message from TCP client {addr}: {tcp_data.decode()}')
                conn.send(b'Hello TCP client')
            else:
                print(f'TCP client {addr} disconnected')
                conn.close()

        elif sock == udp_socket:
            udp_data, addr = udp_socket.recvfrom(1024)
            print(f'Message from UDP client {addr}: {udp_data.decode()}')

            udp_socket.sendto(b'Hello UDP client', addr)
