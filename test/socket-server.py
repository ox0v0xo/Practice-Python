import socket

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务端IP和端口
server_ip = '192.168.209.39'  # 使用主机B的内网IP地址
server_port = 9999

# 绑定IP和端口
server_socket.bind((server_ip, server_port))

# 开始监听，参数指定最大的连接请求的队列长度
server_socket.listen(5)

print(f"服务端启动，监听IP：{server_ip}，端口：{server_port}")

while True:
    # 接受客户端的连接
    client_socket, client_address = server_socket.accept()
    print(f"接受来自 {client_address} 的连接")

    # 接收客户端发送的数据（小于1024字节）
    message = client_socket.recv(1024).decode()
    print(f"从客户端接收到的消息：{message}")

    # 向客户端发送响应
    client_socket.send('消息已收到'.encode())

    # 关闭客户端连接
    client_socket.close()