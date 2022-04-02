class Player:
    __selection = 'Papel'

    def __init__(self, ip):
        self.__ip = ip

    def setType(self, selection):
        self.__selection = selection
    
    def getSelection(self):
        return self.__selection
    
    def whatHappensAgainst(self,selection):
        if self.__selection == 'Pedra':
            if selection == 'Pedra':
                return 'draws'
            elif selection == 'Tesoura':
                return 'wins'
            else:
                return 'loses'
        elif self.__selection == 'Tesoura':
            if selection == 'Pedra':
                return 'loses'
            elif selection == 'Tesoura':
                return 'draws'
            else:
                return 'wins'
        else:
            if selection == 'Pedra':
                    return 'wins'
            elif selection == 'Tesoura':
                return 'loses'
            else:
                return 'draws'
        

class Game:
    currentMatchResult = 'draws' #comeca em empate para que o jogo continue rodando
    bothPlayersConnected = False #se os dois players nao estiverem conectados isso deve iniciar como falso

    def __init__(self, type1, type2):
        while not(self.bothPlayersConnected):
            player1 = Player('192.168.0.7') #socket
            player2 = Player('192.168.0.8') #socket
            break #nao temos o teste pra verificar se os player estao conectados ainda, entao quebra o loop mesmo

        while self.currentMatchResult == 'draws':

            player1.setType(type1) #escolha do player1
            player2.setType(type2) #escolha do player2

            self.currentMatchResult = player1.whatHappensAgainst(player2.getSelection())
            if self.currentMatchResult == 'wins':
                print('player1 wins!')
                break
            elif self.currentMatchResult == 'loses':
                print('player2 wins!')
                break
            else:
                print('empate!')
                #repeat match

import socket

class Player:
    __selection = 'Papel'

    def __init__(self, ip):
        self.__ip = ip

    def setType(self, selection):
        self.__selection = selection
    
    def getSelection(self):
        return self.__selection
    
    def whatHappensAgainst(self,selection):
        if self.__selection == 'Pedra':
            if selection == 'Pedra':
                return 'draws'
            elif selection == 'Tesoura':
                return 'wins'
            else:
                return 'loses'
        elif self.__selection == 'Tesoura':
            if selection == 'Pedra':
                return 'loses'
            elif selection == 'Tesoura':
                return 'draws'
            else:
                return 'wins'
        else:
            if selection == 'Pedra':
                    return 'wins'
            elif selection == 'Tesoura':
                return 'loses'
            else:
                return 'draws'
        

class Game:
    currentMatchResult = 'draws' #comeca em empate para que o jogo continue rodando
    bothPlayersConnected = False #se os dois players nao estiverem conectados isso deve iniciar como falso

    def __init__(self, type1, type2):
        while not(self.bothPlayersConnected):
            player1 = Player('192.168.0.7') #socket
            player2 = Player('192.168.0.8') #socket
            break #nao temos o teste pra verificar se os player estao conectados ainda, entao quebra o loop mesmo

        while self.currentMatchResult == 'draws':

            player1.setType(type1) #escolha do player1
            player2.setType(type2) #escolha do player2

            self.currentMatchResult = player1.whatHappensAgainst(player2.getSelection())
            if self.currentMatchResult == 'wins':
                print('player1 wins!')
                break
            elif self.currentMatchResult == 'loses':
                print('player2 wins!')
                break
            else:
                print('empate!')
                #repeat match


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
            ext = str(info[1].rpartition(b'.')[-1])
            f = open(info[1][1:], 'rb')
            figure = f.read()
            
            conn.sendall('HTTP/1.0 200 OK\r\n' +
                         'Content-Type: image' + ext + '\r\n' +
                         'Content-Length: ' + str(len(figure)) + '\r\n\r\n' +
                          figure)
    
    conn.close()
s.close()