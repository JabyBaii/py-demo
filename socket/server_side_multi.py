import socket
import threading


def handle_client_request(service_client_socket, ip_port):

    # 循环发送数据
    while True:
        recv_data = service_client_socket.recv(1024)  # 接收C端1024字节数据
        if recv_data:
            recv_data_length = len(recv_data)  # 数据实际长度
            print("接收数据的长度为:", recv_data_length)
            recv_content = recv_data.decode("gbk")
            print("C说：", recv_content)

            # 接收到数据，此时服务端发送数据给客户端
            send_data = "收到，问题正在处理中，请稍后".encode("gbk")
            service_client_socket.send(send_data)
        else:
            print("未收到数据，C端掉线了", ip_port)
            break

    service_client_socket.close()   # 终止通信


if __name__ == '__main__':

    # server socket主要用于监听新连接
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8989))
    # 最大连接数并开启监听
    tcp_server_socket.listen(128)
    print("server持续监听中...")

    # 多线程处理多客户端请求与通信
    while True:
        # 创建另一个用与C/S数据收发的socket
        # 阻塞并等待客户端连接
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("新连接成功，客户端的ip、port：", ip_port)
        # 为每一个新连接创建子线程进行通信
        sub_thread = threading.Thread(target=handle_client_request, args=(service_client_socket, ip_port))

        # 设置守护主线程 并启动子线程
        sub_thread.daemon = True
        sub_thread.start()

    # tcp_server_socket.close()       # 终止监听
