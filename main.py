import socket

h = open('index.html', 'r') #h é a variável que recebe o nosso site
homepage = h.read() #homepage é a variável que possui em formato string o site
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
            ext = str(info[1].rpartition(b'.')[-1]) #ext se refere à extensão do arquivo
            f = open(info[1][1:], 'rb') #variável que abre o arquivo
            fileRequested = f.read() #variável que possue o arquivo em formato de bytes
            resp = str.encode('HTTP/1.0 200 OK\r\n' +
                         'Content-Type: file' + ext + '\r\n' +
                         'Content-Length: ' + str(len(fileRequested)) + '\r\n\r\n')
            conn.sendall(resp + fileRequested) #envia em bytes o cabeçalho + o arquivo
        conn.close() #fechamento de conexão, os arquivos já foram processados.
    else: #se não há pedido por dados (ausência de GET), é uma conexão mal formulada
        print('did not get the request')
        resp = str.encode('HTTP/1.0 469 BAD REQUEST\r\n')
        conn.sendall(resp)

