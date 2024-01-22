import socket

def main():
    # 创建一个TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 定义服务器的IP地址和端口号
    server_ip = "10.149.3.123"
    server_port = 12346
    
    # 连接到服务器
    client_socket.connect((server_ip, server_port))
    
    # 输入要发送的文件名
    file_name = input("请输入要发送的文件名: ")
    
    # 发送文件名给服务器
    client_socket.send(file_name.encode())
    
    # 打开文件并发送文件数据
    try:
        with open(file_name, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
        print(f"文件 '{file_name}' 发送成功")
    except FileNotFoundError:
        print(f"文件 '{file_name}' 不存在")
    
    # 关闭客户端连接
    client_socket.close()

if __name__ == "__main__":
    main()
