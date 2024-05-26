# socket客户端开发
import socket
socket_client = socket.socket()
# 连接服务端
socket_client.connect(("localhost",8888))

while True:
    # 发消息
    msg = input("输入你要和服务端发送的消息：")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))
    recv_data = socket_client.recv(1024).decode("UTF-8")
    print(f"服务端回复的消息是：{recv_data}")

# 关闭连接
socket_client.close()