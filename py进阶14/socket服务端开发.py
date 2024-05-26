# socket服务端开发
"""
什么是socket连接
socket是进程之间通信的一个工具
"""
import socket
# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost",8888))      # Ctrl p看出要传入二元组
# 监听端口
socket_server.listen(1)     # 接受一个整数传参，表示接受的连接数量
# 等待客户端连接
# result:tuple = socket_server.accept()   # accept返回一个双元组
# conn = result[0]      # 客户端和服务端的连接对象
# address = result[1]   # 客户端的地址信息
conn,address = socket_server.accept()   # accept方法是阻塞方法，等待客户端连接，如果没连，就卡这了
print(f"接收到了客户端的连接，客户端的地址信息是：{address}")
while True:
    # 接收客户端信息,使用本次连接对象，即conn
    data = conn.recv(1024).decode("UTF-8")  # recv接收的参数是缓冲区大小，一般为1024
    # recv方法的返回值是bytes对象，可以通过decode方法UTF-8编码转换为字符串对象，该方法也是阻塞方法
    print(f"客户端发来的消息是:{data}")
    msg = input("请输入你要和客户端回复的消息：")  # encode编码将字符串变为bytes
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))
# 关闭连接
conn.close()
socket_server.close()
