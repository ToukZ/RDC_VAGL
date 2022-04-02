import socket

h = open('index.html', 'r')
homepage = h.read()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 42069))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(2000)
    info = data.split(b' ') #GET / HTTP/1.0 -> [GET, /, HTTP/1.0]
    #print(P)
    if info[0] == b'GET':
        if info[1] == b'/':
            resp = ('HTTP/1.0 200 OK\r\n' + 'Content-Type: text/html\r\n' + 'Content-Length: ' + str(len(homepage)) + '\r\n\r\n' + (homepage))
            resp = str.encode(resp)
            conn.sendall(resp)
        else:
            resp = str.encode('HTTP/1.0 404 NOT FOUND\r\n')
            conn.sendall(resp)
        conn.close()
s.close()

