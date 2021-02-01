# coding: utf-8

# ソケット通信(クライアント側)
import socket

ip1 = '192.168.100.151'
port1 = 8765
server1 = (ip1, port1)

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(server1)

line = ''
while line != 'bye':
    # 標準入力からデータを取得
    print('偶数の数値を入力して下さい')
    line = input('>>>')
    
    # サーバに送信
    socket1.send(line.encode("UTF-8"))
    
    # サーバから受信
    data1 = socket1.recv(4096).decode()
    
    # サーバから受信したデータを出力
    print('サーバーからの回答: ' + str(data1))

socket1.close()
print('クライアント側終了です')