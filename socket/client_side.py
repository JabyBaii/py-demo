import socket
import time


if __name__ == '__main__':

    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.3.37", 8989))
    send_data = "你好，这个问题麻烦解决一下"
    print("我说：", send_data)
    tcp_client_socket.send(send_data.encode("gbk"))

    # 收到响应
    for i in range(1000):
        recv_data = tcp_client_socket.recv(1024)    # 接收1024字节大小数据
        recv_content = recv_data.decode("gbk")
        print("S回复：", recv_content)

        time.sleep(0.2)
        send_data = f"在吗？(第 {i} 次请求)"
        print("\n我说：", send_data)
        tcp_client_socket.send(send_data.encode("gbk"))

    tcp_client_socket.close()   # 关闭socket

