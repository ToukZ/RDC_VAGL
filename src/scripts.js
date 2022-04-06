      const rockButton = document.querySelector('#pedra') //Salva numa variável o botão de pedra
      const paperButton = document.querySelector('#papel') //Salva numa variável o botão de papel
      const scissorsButton = document.querySelector('#tesoura') //Salva numa variável o botão de tesoura
      // As buscas na DOM (árvore de elementos do HTML foram feitas por meio do 'id' dos botões)

      // Função que recebe a entrada do jogador e do computador e retorna a mensagem com o resultado para o jogador
      function getPlayerResultMessage(playerEntry, computerEntry) {
        /* 
        - Objetos em javascript podem ser acessados da seguinte forma: objeto['propriedade do objeto']
        - O objeto 'possibilities' abaixo é é um objeto em que suas propriedades também são objetos!
        - Cada propriedade do objeto 'possibilities' é outro objeto com o nome das jogadas possíveis
        e cada objeto desse contém os resultados para o que o computador jogar
        */
        const possibilities = {
          rock: {
            rock: 'Empate!\n\nmelhor escolha não tem ༼  ͡° ͜ʖ ͡° ༽',
            paper: 'Você perdeu, tente novamente!\n\nrulado ¯\\_(ツ)_/¯',
            scissors: 'Parabéns, você ganhou!\n\npedra abuser ( ͡° ͜ʖ ͡°)╭∩╮',
          },
          paper:  {
            rock: 'Parabéns, você ganhou!\nimpossivel, pedra nunca perde\n (╯ ͠° ͟ʖ ͡°)╯┻━┻',
            paper: 'Empate!\n\nimagina jogar de papel',
            scissors: 'Você perdeu, tente novamente!\n\nGit Gud'
          },
          scissors: {
            rock: 'Você perdeu, tente novamente!\n\nGood old rock, nothing beats that ( ͡~ ͜ʖ ͡°)',
            paper: 'Parabéns, você ganhou!\n\ndevia ter jogado pedra ( ͡° ʖ̯ ͡°)',
            scissors: 'Empate!\n\n ( ͡° ͜ʖ ͡°)',
          },
        }

        return possibilities[playerEntry][computerEntry]
      }

      const resultBox = document.querySelector('#resultado') // Salva o elemento html onde vai ser exibido o html

      // Função para mostrar no html o resultado do jogo
      function play(playerMove) {
        const options = ['rock', 'paper', 'scissors'] // Opções de jogo possíveis
        const computerMove = options[Math.floor(Math.random() * options.length)] // Gera uma opção aleatória como jogada do computador

        // Coloca o resultado da combinação jogada-do-jogador & jodada-do-computador no texto do elemento html 
        resultBox.innerText = getPlayerResultMessage(playerMove, computerMove) + '\nO computador escolheu: '+ computerMove
      }

      rockButton.addEventListener('click', () => play('rock')) // Adiciona a função play passando 'rock' como argumento ao botão de pedra
      paperButton.addEventListener('click', () => play('paper')) // Adiciona a função play passando 'paper' como argumento ao botão de papel
      scissorsButton.addEventListener('click', () => play('scissors')) // Adiciona a função play passando 'scissors' como argumento ao botão de tesoura
