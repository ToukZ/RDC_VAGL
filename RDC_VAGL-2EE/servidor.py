import socket
import random
from os import system
from time import sleep
from pygame import mixer

HOST = '192.168.0.4' # IPV4 da maquina que ira rodar o servidor
PORT = 50000 # Porta qualquer (recomendado 5 digitos)

mixer.init()
def defineWinner(choiceServer,choiceClient): # codigo que define o vencedor do embate
    if choiceServer in ['tesoura', 't', 'T']:
        if choiceClient in ['tesoura', 't', 'T']:
            return 'Empate'
        elif choiceClient in ['pedra', 'pe', 'Pe']:
            return 'Client'
        elif choiceClient in ['papel', 'pa', 'Pa']:
            return 'Server'
        else:
            return '400 Bad Client Input' # cliente colocou algo que nao eh reconhecido
    elif choiceServer in ['pedra', 'pe', 'Pe']:
        if choiceClient in ['tesoura', 't', 'T']:
            return 'Server'
        elif choiceClient in ['pedra', 'pe', 'Pe']:
            return 'Empate'
        elif choiceClient in ['papel', 'pa', 'Pa']:
            return 'Client'
        else:
            return '400 Bad Client Input' # cliente colocou algo que nao eh reconhecido
    elif choiceServer in ['papel', 'pa', 'Pa']:
        if choiceClient in ['tesoura', 't', 'T']:
            return 'Client'
        elif choiceClient in ['pedra', 'pe', 'Pe']:
            return 'Server'
        elif choiceClient in ['papel', 'pa', 'Pa']:
            return 'Empate'
        else:
            return '400 Bad Client Input' # cliente colocou algo que nao eh reconhecido
    else:
        return '400 Bad Server Input' # servidor colocou algo que nao eh reconhecido

def frase(result,streak):
    victory = streak + 1
    elogios1=['bom','massa','nice','good','doce vitoria']
    elogios2=['STONKS','UOU','BRABO','ARREBENTOU']
    elogios3=['OVERSTONKS','PRO INFINITO','DESTRUIU','HACKER','CHEATER','IMPOSSIVEL!!!','0.4115%']
    losing=['mais sorte da proxima vez','keke','aaaaaa','n foi dessa vez','tente outra vez']
    if result=='Server':
        if streak<=2:
            print(random.choice(elogios1) + '  streak: ' + f'{victory}')
        elif streak>2 and streak<4:
            print(random.choice(elogios2).upper() + '  ' + f'{victory}' + ' vitorias em sequencia!')
        else:
            print(random.choice(elogios3).upper() + '  ' + '5+ ANIQUILACOES SEGUIDAS!')
    else:
        print(random.choice(losing))


# familia ipv4, protocolo tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))  # vincular host e porta com o socket
s.listen(2)

print('servidor: aguardando conexão de um cliente')
conn, ender = s.accept()  # retorna conexao e endereco
print('Conectado no endereço ', ender)
server_selection = 'pedra' # default soh pra nao bugar
winStreakServer = 0
soundFile = ['1_streak.mp3', '2_streak.mp3', '3_streak.mp3', '4_streak.mp3', '5_streak.mp3']

while(True):
    print('Aguardando Cliente fazer sua selecao')
    data = conn.recv(1024)  # recebe a selecao do cliente
    client_selection = data.decode() # decodifica ela
    
    if not data:  # quando nao tiver mais dados entra aqui
        conn.close()  # fecha a conexao
        break  # interrompe o loop
    else:
        system('cls')
        server_selection = input('servidor, digite a sua selecao: ') # input do servidor
        conn.sendall(server_selection.lower().encode()) # envia a resposta do servidor
        result = defineWinner(server_selection.lower(), client_selection.lower()) # calcula resultado do embate
        str = ('o vencedor eh: ' + result) # formatacao
        print(str + '\nA escolha do cliente foi: ' + client_selection + '\n') # resultado do embate formatado
        frase(result, winStreakServer)
        if result == 'Server':
            mixer.music.load('music/' + soundFile[winStreakServer])
            mixer.music.play()
            winStreakServer += 1
            if winStreakServer > 4:
                winStreakServer -= 1
        elif result == 'Client':
            winStreakServer = 0
        conn.sendall(result.encode()) # envia o resultado do embate
        conn.sendall(str.encode()) # envia o resultado do embate formatado
        input('\n\n Pressione Enter para continuar...')
        system('cls')
