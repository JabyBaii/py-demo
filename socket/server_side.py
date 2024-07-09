import socket


if __name__ == '__main__':

    # server socket主要用于监听新连接
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8989))
    # 最大连接数并开启监听
    tcp_server_socket.listen(128)
    print("server持续监听中...")

    # 创建另一个用与C/S数据收发的socket
    # 阻塞并等待客户端连接
    service_client_socket, ip_port = tcp_server_socket.accept()
    print("新连接成功，客户端的ip、port：", ip_port)
    recv_data = service_client_socket.recv(1024)    # 接收C端1024字节数据
    recv_data_length = len(recv_data)               # 数据实际长度
    print("接收数据的长度为:", recv_data_length)
    recv_content = recv_data.decode("gbk")
    print("C说：", recv_content)

    # 接收到数据，此时服务端发送数据给客户端
    send_data = "收到，问题正在处理中，请稍后".encode("gbk")
    service_client_socket.send(send_data)

    service_client_socket.close()   # 终止通信
    tcp_server_socket.close()       # 终止监听
