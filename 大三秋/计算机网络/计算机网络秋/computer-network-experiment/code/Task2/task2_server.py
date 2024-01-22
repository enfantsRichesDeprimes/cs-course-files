import socket
import os

def main():
    # 创建一个TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 定义服务器的IP地址和端口号
    server_ip = "10.149.0.154"
    server_port = 12346
    
    # 绑定服务器地址和端口
    server_socket.bind((server_ip, server_port))
    
    # 开始监听客户端连接
    server_socket.listen(5)
    print(f"服务器正在监听 {server_ip}:{server_port}")
    
    # 创建保存文件的文件夹
    if not os.path.exists("server_files"):
        os.makedirs("server_files")
    
    while True:
        # 等待客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"与客户端 {client_address} 建立连接")
        
        # 接收文件名
        file_name = client_socket.recv(1024).decode()
        file_path = os.path.join("server_files", file_name)
        
        try:
            # 接收文件数据并保存到本地文件
            with open(file_path, "wb") as file:
                data = client_socket.recv(1024)
                while data:
                    file.write(data)
                    data = client_socket.recv(1024)
            print(f"文件 '{file_name}' 接收成功并保存在 'server_files' 文件夹中")
        except Exception as e:
            print(f"文件 '{file_name}' 接收失败: {e}")
        
        # 关闭客户端连接
        client_socket.close()

if __name__ == "__main__":
    main()
