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

Game('Papel', 'Pedra')