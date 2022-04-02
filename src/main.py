import socket

h = open('index.html', 'r') #h é a variável que recebe o nosso site
homepage = h.read() #homepage é a variável que possui em bytes o site
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #abertura do socket para conexão
s.bind(('', 42069)) #abrir o socket localmente com porta 42069
s.listen(1) #espera receber 1 conexão

while True: #enquanto tiver conexão, vai continuar rodando
    conn, addr = s.accept() #variável que salva os dados da conexao
    data = conn.recv(2000) #variável que aceita até 2000 bytes dos dados recebidos
    info = data.split(b' ') #variável que separa os dados recebidos por espaços em um vetor

    if info[0] == b'GET': #se há um pedido por dados
        print('got request, ')
        if info[1] == b'/': #envie a página da web se ele quer uma pagina da web
            print('webpage got sent')
            resp = ('HTTP/1.0 200 OK\r\n' + 'Content-Type: text/html\r\n' + 'Content-Length: ' + str(len(homepage)) + '\r\n\r\n' + (homepage))
            resp = str.encode(resp)
            conn.sendall(resp)
        else: #envie o arquivo requerido pela request
            print('file was sent: ' + str(info[1]))
            ext = str(info[1].rpartition(b'.')[-1])
            f = open(info[1][1:], 'rb')
            fileRequested = f.read()
            resp = str.encode('HTTP/1.0 200 OK\r\n' +
                         'Content-Type: file' + ext + '\r\n' +
                         'Content-Length: ' + str(len(fileRequested)) + '\r\n\r\n')
            conn.sendall(resp + fileRequested)
        conn.close()
    else: #se não há pedido por dados, é uma conexão mal formulada
        print('did not get a request')
        resp = str.encode('HTTP/1.0 469 BAD REQUEST\r\n')
        conn.sendall(resp)

