import socket
import random
from os import system
from time import sleep
from pygame import mixer

HOST = '192.168.0.4'  # endereco do servidor
PORT = 50000  # mesma porta do servidor para garantir a conexao

mixer.init()
def frase(result,streak):
    victory = streak
    elogios1=['bom','massa','nice','good','doce vitoria']
    elogios2=['stonks','UOU','brabo','arrebentou']
    elogios3=['OVERSTONKS','PRO INFINITO','DESTRUIU','hacker','cheater','0.4115%','IMPOSSIVEL!!!']
    losing=['mais sorte da proxima vez','keke :c','aaaaaa','n foi dessa vez','tente outra vez', 'tururuuu...']
    if result=='Client':
        if streak<=3:
            print(random.choice(elogios1) + '  streak: ' + f'{victory}')
        elif streak>3 and streak<=4:
            print(random.choice(elogios2).upper() + '  ' + f'{victory}' + ' vitorias em sequencia!')
        else:
            print(random.choice(elogios3).upper() + '  ' + '5+ ANIQUILACOES SEGUIDAS!')
    else:
        print(random.choice(losing))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # conecta no servidor na porta referida
client_selection = 'pedra' # default soh pra nao bugar
winStreakClient = 0
soundFile = ['1_streak.mp3', '2_streak.mp3', '3_streak.mp3', '4_streak.mp3', '5_streak.mp3', '5_streak.mp3']

while(True):
    system('cls')
    client_selection = input('cliente, digite pedra, papel ou tesoura: ') # input do cliente
    s.sendall(client_selection.encode()) # envia selecao do cliente
    print('Aguardando o Servidor fazer sua selecao')
    server_selection = s.recv(1024)  # recebe a selecao do servidor codificada
    result = s.recv(1024) # recebe o resultado do embate codificado
    data = s.recv(1024) # recebe o resultado do embate codificado e formatado

    if result.decode() == 'Client':
        mixer.music.load('music/' + soundFile[winStreakClient])
        mixer.music.play()
        winStreakClient += 1
        if winStreakClient > 5:
            winStreakClient -= 1
    elif result.decode() == 'Server':
        winStreakClient = 0

    print(data.decode()) # decodifica o resultado do embate formatado
    print('A escolha do Servidor foi: ', server_selection.decode() + '\n') # resultado do embate decodificado e formatado
    frase(result.decode(), winStreakClient)
    input('\n\n Pressione Enter para continuar...')
print('\ncabou') # fim do programa