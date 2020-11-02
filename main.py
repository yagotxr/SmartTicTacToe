from gameMaker import gameMaker
  
print("|X|X|X||- Jogo da Velha -||O|O|O|")

def start():
    try:
        level = int(input("Selecione o nivel de dificuldade: \n1- Fácil\n2- Médio\n3- Difícil\n=> "))
        print(level)
        game = gameMaker(level)
        game.play()
    except:
        print('Level inválido. Tente novamente.')
        start()

start()